from discongas.undisturbedremoval import *
from discongas.util.inputoutput import *
from discongas.util.roof import *
import sys
import pandas as pd

class Model():
  @classmethod
  def from_csv(cls, filepath):
    df = pd.read_csv(filepath)
    buildingdict = df[df['schornstein']==True].to_dict(orient='records')
    if len(buildingdict) > 0:
      if len(buildingdict) > 1:
        raise ValueError('Multiple source roofs are not supported.')
      sourceroof = Roof.from_dict(buildingdict[0])
      a = buildingdict[0]['a']
    else:
      raise ValueError('There must be a source roof defined.')

    m = Model(a, sourceroof)

    upstreamroofs = df[df['schornstein']==False].to_dict(orient='records')
    for ur in upstreamroofs:
      r = Roof.from_dict(ur)
      m.add_upstreamroof(ur['beta'], ur['l_a'], r)

    return m

  def __init__(self, a, sourceroof):
    self.a = a
    self.sourceroof = sourceroof
    self.upstreamroofs = {}
    self.data = {}
    self.__add_roof_data(sourceroof)
    self.__add_data(sourceroof, "A", a)

  def add_upstreamroof(self, beta, l_A, upstreamroof):
    self.upstreamroofs[upstreamroof.name] = {}
    self.upstreamroofs[upstreamroof.name]['r'] = upstreamroof
    self.upstreamroofs[upstreamroof.name]['beta'] = beta
    self.upstreamroofs[upstreamroof.name]['l_A'] = l_A

    self.__add_roof_data(upstreamroof)
    self.__add_data(upstreamroof, "Beta", beta)
    self.__add_data(upstreamroof, "L_A", l_A)

  def add_referencelevel(self, H_F, upstreamroof):
    if upstreamroof.name in self.upstreamroofs.keys():
      self.upstreamroofs[upstreamroof.name]['H_F'] = H_F
      self.__add_data(upstreamroof, "H_F", H_F)
    else: 
      raise ValueError("No upstream roof with name: '{}' exists. First add upstream roof before defining reference level.".format(upstreamroof.name))

  def heightbyundisturbedremoval(self):
    H_A1 = self.sourceroof.H_A1(self.a)
    self.__add_data(self.sourceroof, "H_A1", H_A1)

    H_A2 = -sys.maxsize
    for key in self.upstreamroofs.keys():
      
      dur = self.upstreamroofs[key]
      ur = dur['r']

      L_RZ = ur.L_RZ(dur['beta'])

      self.__add_data(ur, "L_RZ", L_RZ)

      if dur['l_A'] <= L_RZ:
        hH_A2 = ur.H_A2(dur['beta'], dur['l_A'], self.sourceroof.H_First, self.sourceroof.H_U)
        hH_A2T = 0

        heightdifference = ur.h - self.sourceroof.h
        if heightdifference != 0:
          hH_A2T = hH_A2 + heightdifference
          hH_A2 = 0
           
        if hH_A2 > H_A2 or hH_A2T > H_A2:
          self.H_A_source = key
          H_A2 = hH_A2 if hH_A2 > 0 else hH_A2T

        self.__add_data(ur, "H_A2", hH_A2)
        self.__add_data(ur, "H_A2T", hH_A2T)
    
    if H_A1 > H_A2:
      self.H_A_source = self.sourceroof.name
      return round(H_A1, 1)
    return round(H_A2, 1)

  def heightbyadequatedilution(self):
    if self.sourceroof.ratedthermalinput > 1:
      H_E1 = self.sourceroof.H_E1()
      self.__add_data(self.sourceroof, "H_E1", H_E1)
    else:
      H_E1 = 0

    H_E2 = -sys.maxsize
    for key in self.upstreamroofs.keys():
      dur = self.upstreamroofs[key]
      if 'H_F' in dur.keys():
        ur = dur['r']
        hH_E2 = self.sourceroof.H_E2(dur['H_F'])
        hH_E2T = 0
        heightdifference = ur.h - self.sourceroof.h
        if heightdifference != 0:
          hH_E2T = hH_E2 + heightdifference
          hH_E2 = 0

        if hH_E2 > H_E2 or hH_E2T > H_E2:
          self.H_E_source = key
          H_E2 = hH_E2 if hH_E2 > 0 else hH_E2T

        self.__add_data(ur, "H_E2", hH_E2)
        self.__add_data(ur, "H_E2T", hH_E2T)

    if H_E1 > H_E2 and H_E1 > 0:
      self.H_E_source = self.sourceroof.name
      return round(H_E1, 1)
    return round(H_E2, 1)

  def height(self):
    self.hbur = self.heightbyundisturbedremoval()
    self.hbad = self.heightbyadequatedilution()

    if self.hbur > self.hbad:
      self.H_source = "Undisturbed Removal"
      return self.hbur
    self.H_source = "Adequate Dilution"
    return self.hbad

  def __add_roof_data(self, roof):
    if roof.name not in self.data.keys():
      self.data[roof.name] = roof.as_dict()

  def __add_data(self, roof, key, value):
    self.data[roof.name][key] = round(value, 1)

  def height_with_dict(self):
    height = self.height()
    
    #if self.H_source == "UR":
      #return height, "UR", self.H_A_source, self.data
    #return height, "AD", self.H_E_source, self.data

    res = {
      'Source Roof': self.sourceroof.name,
      'Number of upstream roofs': len(self.upstreamroofs),
      'Result': {
        'Height': height,
        'Source': self.H_source,
      },
      'Adequate Dilution': {
        'Height': self.hbad,
        'Source': self.H_E_source
      },
      'Undisturbed Removal': {
        'Height': self.hbur,
        'Source': self.H_A_source
      },
      'Data': self.data
    }

    return res