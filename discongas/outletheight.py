from discongas.undisturbedremoval import *
from discongas.util.inputoutput import *
from discongas.util.roof import *
import sys
import numpy as np

class Model():

  def __init__(self, a, sourceroof, nominalheatoutput=400, ratedthermalinput=0.9):
    self.a = a
    self.sourceroof = sourceroof
    self.upstreamroofs = []
    self.H_U = additiveterm(nominalheatoutput, ratedthermalinput)
    self.nominalheatoutput=nominalheatoutput
    self.ratedthemalinput=ratedthermalinput
    self.H_B = H_B(nominalheatoutput)

  def exposure_zone(self):
    """
    Exposure zone of the exhaust gas discharge system

    :return: radius of the exposure zone (in m)
    """
    return exposurezone(self.nominalheatoutput)

  def add_upstreamroof(self, beta, l_A, upstreamroof, H_F=None):
    self.upstreamroofs.append((upstreamroof, beta, l_A, H_F))

  def H_A1(self):
    return self.sourceroof.H_A1(self.a, self.H_U)
  
  def H_A2(self):
    H_A2 = -sys.maxsize
    H_A2_source = None, None, None, None
    H_First = self.sourceroof.H_First
    for v in self.upstreamroofs:
      ur = v[0]
      beta = v[1]
      l_A = v[2]

      L_RZ = ur.L_RZ(beta)

      if l_A <= L_RZ:
        hH_A2 = ur.H_A2(beta, l_A, H_First, self.H_U)
           
        if hH_A2 > H_A2:
          H_A2 = hH_A2
          H_A2_source = v
    return H_A2_source
  
  def H_A2T(self):
    H_A2 = -sys.maxsize
    H_A2T_source = None, None, None, None
    H_First = self.sourceroof.H_First
    for v in self.upstreamroofs:
      ur = v[0]
      beta = v[1]
      l_A = v[2]

      L_RZ = ur.L_RZ(beta)

      if l_A <= L_RZ:
        hH_A2T = ur.H_A2T(beta, l_A, H_First, self.H_U, self.sourceroof.h)
           
        if hH_A2T > H_A2:
          H_A2 = hH_A2T
          H_A2T_source = v
    return H_A2T_source

  def H_A(self):
    self.H_A1_source = self.sourceroof
    H_A1 = self.H_A1()

    H_A2_values = self.H_A2()
    self.H_A2_source, H_A2_beta, H_A2_lA, _ = H_A2_values
    H_A2 = self.H_A2_source.H_A2(H_A2_beta, H_A2_lA, self.sourceroof.H_First, self.H_U) if self.H_A2_source is not None else -sys.maxsize
    
    H_A2T_values = self.H_A2T()
    self.H_A2T_source, H_A2T_beta, H_A2T_lA, _ = H_A2T_values
    H_A2T = self.H_A2T_source.H_A2T(H_A2T_beta, H_A2T_lA, self.sourceroof.H_First, self.H_U, self.sourceroof.h) if self.H_A2T_source is not None else -sys.maxsize

    H_A_values = [H_A1, H_A2, H_A2T]
    imax = np.argmax(H_A_values)
    self.H_A_source = [self.H_A1_source, self.H_A2_source, self.H_A2T_source][imax]

    return H_A_values[imax]
  
  def H_E1(self):
    return self.sourceroof.H_E1(self.ratedthemalinput)

  def H_E2(self):
    H_E2 = -sys.maxsize
    H_E2_source = None, None, None, None
    H_First = self.sourceroof.H_First
    for v in self.upstreamroofs:
      ur = v[0]
      H_F = v[3]
      if H_F is not None:
        hH_E2 = ur.H_E2(H_F, self.H_B, H_First)
        if hH_E2 > H_E2:
          H_E2 = hH_E2
          H_E2_source = v
    return H_E2_source
  
  def H_E2T(self):
    H_E2T = -sys.maxsize
    H_E2T_source = None, None, None, None
    H_First = self.sourceroof.H_First
    for v in self.upstreamroofs:
      ur = v[0]
      H_F = v[3]
      if H_F is not None:
        hH_E2T = ur.H_E2T(H_F, self.H_B, H_First, ur.h)
        if hH_E2T > H_E2T:
          H_E2T = hH_E2T
          H_E2T_source = v
    return H_E2T_source
  
  def H_E(self):
    self.H_E1_source = self.sourceroof
    H_E1 = self.H_E1()

    H_E2_values = self.H_E2()
    self.H_E2_source,_ ,_ , H_F = H_E2_values
    H_E2 = self.H_E2_source.H_E2(H_F, self.H_B, self.sourceroof.H_First) if self.H_E2_source is not None else -sys.maxsize
    
    H_E2T_values = self.H_E2T()
    self.H_E2T_source,_ ,_ , H_F = H_E2T_values
    H_E2T = self.H_E2T_source.H_E2T(H_F, self.H_B, self.sourceroof.H_First, self.sourceroof.h) if self.H_E2T_source is not None else -sys.maxsize

    H_E_values = [H_E1, H_E2, H_E2T]
    print(H_E_values)
    imax = np.argmax(H_E_values)
    self.H_E_source = [self.H_E1_source, self.H_E2_source, self.H_E2T_source][imax]

    return H_E_values[imax]

  def height(self):
    H_A = self.H_A()
    H_E = self.H_E()

    if H_E is not None and H_E > H_A:
      self.H_source = self.H_E_source
    else:
      self.H_source = self.H_A_source

    return max(H_A, H_E)