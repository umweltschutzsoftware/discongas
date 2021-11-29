from discongas.undisturbedremoval import *
from discongas.util.inputoutput import *
from discongas.util.roof import *

class Model():
  def __init__(self, a, sourceroof):
    self.a = a
    self.sourceroof = sourceroof
    self.upstreamroofs = {}

  def add_upstreamroof(self, beta, l_A, upstreamroof):
    self.upstreamroofs[upstreamroof.name] = {}
    self.upstreamroofs[upstreamroof.name]['r'] = upstreamroof
    self.upstreamroofs[upstreamroof.name]['beta'] = beta
    self.upstreamroofs[upstreamroof.name]['l_A'] = l_A

  def add_referencelevel(self, H_F, upstreamroof):
    if upstreamroof.name in self.upstreamroofs.keys():
      self.upstreamroofs[upstreamroof.name]['H_F'] = H_F
    else: 
      raise ValueError("No upstreamroof with name: '{}' exists. First add upstream roof before defining reference level.".format(upstreamroof.name))

  def heightbyundisturbedremoval(self):
    H_A1 = self.sourceroof.H_A1(self.a)

    H_A2 = []
    H_A2T = []
    for key in self.upstreamroofs.keys():
      dur = self.upstreamroofs[key]
      ur = dur['r']
      if dur['l_A'] <= ur.L_RZ(dur['beta']):
        hH_A2 = ur.H_A2(dur['beta'], dur['l_A'], self.sourceroof.H_First, self.sourceroof.H_U)
        hH_A2T = 0
        heightdifference = ur.h - self.sourceroof.h
        if heightdifference != 0:
          hH_A2T = hH_A2 + heightdifference
          hH_A2 = 0
        H_A2T.append(hH_A2T)
        H_A2.append(hH_A2)
    
    if len(H_A2) > 0:
      return round(max(H_A1, max(H_A2), max(H_A2T)),1)
    return round(H_A1, 1)

  def heightbyadequatedilution(self):
    H_E1 = self.sourceroof.H_E1()

    H_E2 = []
    H_E2T = []
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
        H_E2T.append(hH_E2T)
        H_E2.append(hH_E2)
    if len(H_E2) > 0:
      return round(max(H_E1, max(H_E2), max(H_E2T)),1)
    return round(H_E1, 1)

  def height(self):
    return max(self.heightbyundisturbedremoval(), self.heightbyadequatedilution())