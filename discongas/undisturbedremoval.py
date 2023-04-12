import math
from discongas.util.inputoutput import *
from discongas.util.roof import *
from discongas.adequatdilution import *
import copy

from abc import ABC, abstractmethod

class Roof(ABC):
  @classmethod
  def from_roof(cls, orig):
    return cls(orig.name, orig.alpha, orig.H_First, orig.H_Dach, orig.b, orig.l, orig.h, orig.alpha_O, orig.b_O, orig.address)

  def __init__(self, name, alpha, H_First, H_Dach, b, l, h, alpha_O=None, b_O=None, address=None):
    """
    The roof constructor.

    :param name: The name descriptor of the current roof.:
    :param alpha: roof pith angle. In case of a mansard roof, this is the angle of the lower roof. (in degree):
    :param H_First: ridge height of the building with the outlet (in m):
    :param H_Dach: the buildings actual roof height (in m):
    :param b: width of the buildings gable, or the side of the building in direction to the building with the outlet. In case of a mansard roof, this is the width of the lower roof. (in m):
    :param l: length of the building. (in m):
    :param h: height of the ground of the building of the roof. (in m):
    :param ratedthermalinput: Rated thermal input. Default 0.9 (in MW):
    :param alpha_O: in case of a mansard roof, this is the angle of the upper roof. Default: None (in degree):
    :param b_O: in case of a mansard roof, this is the width of the upper roof. Default: None (in m):
    :param address: Adress of the current building:

    """
    self.name = name
    self.alpha = alpha
    self.H_Dach = H_Dach
    self.H_First = H_First
    self.gamma, self.f = roofpitchcorrection(self.alpha)
    self.H_B = -1
    self.b = b
    self.l = l
    self.alpha_O = alpha_O
    self.b_O = b_O
    if self.alpha_O is not None:
      self.gamma_O, self.f_O = roofpitchcorrection(self.alpha_O)
    self.contiguous = False
    self.address = address
    self.h = h

  def L_RZ(self, beta):
    """
    Length of the recirculation zone.

    :param beta: horizontal angle between an upstream building an the direction of the exhaust gas discharge system (in m):

    :return: L_RZ (in m)
    """
    if not self.contiguous:
      L_EFF = self.l * math.sin(beta * math.pi / 180) + self.b * math.cos(beta * math.pi / 180)
      L_RZ = (1.75*L_EFF)/(1+0.25*L_EFF/self.H_First)
    else:
      L_RZ = 6*self.H_First
    return round(L_RZ,1)
  
  def p(self, l_A, l_RZ):
    """
    Interpolation parameter for determining the height of the recirculation zone

    :param l_A: horizontal distance of the exhaust gas discharge system from an upstream building (in m):
    :param l_RZ: Length of the recirculation zone (in m):

    :return: p (in m)
    """
    return math.sqrt(1-((l_A*l_A)/(l_RZ*l_RZ)))
  
  def H_S2(self, l_A, l_RZ, H_First):
    """
    Calculated exhaust gas discharge systems height above the ridge witouht an additive term with upstream buildings

    :param l_A: horizontal distance of the exhaust gas discharge system from an upstream building (in m):
    :param l_RZ: Length of the recirculation zone (in m):
    :param H_First: ridge height of the building with the outlet (in m):

    :return: H_S2 (in m)
    """
    return self.p(l_A, l_RZ)*(self.H_First+self.H_2())-H_First

  def H_A2(self, beta, l_A, H_First, H_U):
    """
    Required height of the exhaust gas discharge systems outlet above the ridge for undisturbed removal of the exhaust gas due to upstream buildings

    :param beta: horizontal angle between an upstream building an the direction of the exhaust gas discharge system (in m):
    :param l_A: horizontal distance of the exhaust gas discharge system from an upstream building (in m):
    :param H_First: ridge height of the building with the outlet (in m):
    :param H_U: correction value of the building with the outlet (in m):

    :return: H_A2 (in m)
    """
    l_RZ = self.L_RZ(beta)
    H_S2 = self.H_S2(l_A, l_RZ, H_First)
    return round(H_S2 + H_U, 1)
  
  def H_A2T(self, beta, l_A, H_First, H_U, h):
    """
    Required height of the exhaust gas discharge systems outlet above the ridge for undisturbed removal of the exhaust gas due to hillside location of a building

    :param beta: horizontal angle between an upstream building an the direction of the exhaust gas discharge system (in m):
    :param l_A: horizontal distance of the exhaust gas discharge system from an upstream building (in m):
    :param H_First: ridge height of the building with the outlet (in m):
    :param H_U: correction value of the building with the outlet (in m):
    :param h: height of the source roof (in m):

    :return: H_A2T (in m)
    """
    heightdifference = self.h - h
    return round(self.H_A2(beta, l_A, H_First, H_U) + heightdifference, 1)

  @abstractmethod
  def H_A1(self, a, H_U):
    """
    Required height of the exhaust gas discharge systems outlet for undisturbed removal of exhaust gas for a single building.

    :param a: horizontal distance beween the centre of the outlet cross-section and the ridge (in m):

    :return: height H_A1 (in m)
    """
    pass

  @abstractmethod
  def H_1(self, a):
    """
    height of the recirculation zone (based on he ridge height) as a function of the distance a

    :param a: horizontal distance beween the centre of the outlet cross-section and the ridge (in m):

    :return: height H_1 (in m)
    """
    pass
  
  @abstractmethod
  def H_2(self):
    """
    Maximal height of the recirculation zone

    :return: height H_2 (in m)
    """
    pass

  def H_E1(self, ratedthermalinput):
    """
    Minimum height of the exhaust gas discharge system above the terrain surface

    :return: H_E1 (in m)
    """
    if ratedthermalinput < 1:
      return 0
    return 10 - self.H_First

  def H_E2(self, H_F, H_B, H_First):
    """
    Required outlet height above the ridge based on the reference level

    :return: H_E2 (in m)
    """
    return round((H_F - H_First) + H_B, 1)
  
  def H_E2T(self, H_F, H_B, H_First, h):
    """
    Required outlet height above the ridge based on the reference level

    :return: H_E2T (in m)
    """
    heightdifference = self.h - h
    return round(self.H_E2(H_F, H_B, H_First) + heightdifference, 1)

class SymmetricPitchedRoof(Roof):
  def H_2(self):
    if self.alpha >= 20:
      return self.f * self.H_Dach
    else:
      f = self.alpha/20*0.85
      return (1+f)*self.b/2*math.tan(20*math.pi/180)-self.H_Dach
    
  def H_1(self, a):
    if self.alpha >= 20:
      return a * math.tan((self.alpha-self.gamma)*math.pi/180)
    else:
      return (a+self.b/2)*math.tan(20*math.pi/180)-self.H_Dach

  def H_A1(self, a, H_U=0.4):
    H_1 = self.H_1(a)
    H_2 = self.H_2()
    H_S1 = min(H_1, H_2)
    return round(H_S1 + H_U, 1)

class FlatRoof(Roof):
  def H_A1(self, a, H_U=0.4):
    # 6.2.1 Eq. 8
    spr = SymmetricPitchedRoof.from_roof(self)
    H_A1 = spr.H_A1(a)
    H_A1F = round(1.3*((self.H_First**2)**(1./3.))+H_U,1)
    return min(H_A1, H_A1F)
  
  def H_1(self, a):
    spr = SymmetricPitchedRoof.from_roof(self)
    return spr.H_1(a)

  def H_2(self):
    spr = SymmetricPitchedRoof.from_roof(self)
    return spr.H_2()

class AsymmetricPitchedRoof(Roof):
  def H_A1(self, a, H_U=0.4):
    # 6.2.1.2.4
    spr = SymmetricPitchedRoof.from_roof(self)
    return spr.H_A1(a, H_U)

  def H_1(self, a):
    spr = SymmetricPitchedRoof.from_roof(self)
    return spr.H_1(a)

  def H_2(self):
    spr = SymmetricPitchedRoof.from_roof(self)
    return spr.H_2()

class SinglePitchRoof(Roof):
  def H_A1(self, a, H_U=0.4):
    H_1 = self.H_1(a)
    H_2 = self.H_2()
    H_S1 = min(H_1, H_2)
    return round(H_S1 + H_U, 1)
  
  def H_1(self, a):
    # 6.2.1.2.5
    if (self.alpha >= 20):
      c = 0
    else: 
      c=(self.b/2-a)*(1-self.alpha/20)
    return (a+c)*math.tan(20*math.pi/180)

  def H_2(self):
    return self.b/2*math.tan(20*math.pi/180)

class SawToothRoof(Roof):
  def H_A1(self, a, H_U=0.4):
    fr = FlatRoof.from_roof(self)
    cfr = copy.copy(fr)
    cfr.H_Dach=0
    r = cfr.H_A1(a, H_U)
    return r
  
  def H_1(self,a):
    fr = FlatRoof.from_roof(self)
    cfr = copy.copy(fr)
    cfr.H_Dach=0
    return cfr.H_1(a)
  
  def H_2(self):
    fr = FlatRoof.from_roof(self)
    cfr = copy.copy(fr)
    cfr.H_Dach=0
    return cfr.H_2()

class HippedRoof(Roof):
  def H_A1(self, a, H_U=0.4):
    spr = SymmetricPitchedRoof.from_roof(self)
    H_A1 = spr.H_A1(a, H_U)

    H_S1 = H_A1 - H_U
    if self.l/self.b <= 1.2:
      return round(H_S1*0.6+H_U, 1)
    return H_A1
  
  def H_1(self, a):
    spr = SymmetricPitchedRoof.from_roof(self)
    return spr.H_1(a)

  def H_2(self):
    spr = SymmetricPitchedRoof.from_roof(self)
    return spr.H_2()

class MansardRoof(Roof):
  def __rO(self):
    spro = SymmetricPitchedRoof.from_roof(self)
    H_DachO  = self.b/2 * math.tan(math.pi*self.alpha_O/180)
    spro.H_Dach = H_DachO
    spro.alpha = self.alpha_O
    spro.f = self.f_O
    spro.gamma = self.gamma_O
    return spro

  def __rU(self):
    spru = SymmetricPitchedRoof.from_roof(self)
    H_DachU = self.b/2 * math.tan(math.pi*self.alpha/180)
    spru.H_Dach = H_DachU
    return spru

  def H_A1(self, a, H_U=0.4):
    H_1 = self.H_1(a)
    H_2 = self.H_2()
    H_S1 = min(H_1, H_2)
    return round(H_S1 + H_U, 1)
  
  def H_1(self, a):
    spro = self.__rO()
    spru = self.__rU()
    H_1O = spro.H_1(a)
    H_1U = spru.H_1(a)
    return self.b_O/self.b*H_1O+(1-self.b_O/self.b)*H_1U

  def H_2(self):
    spro = self.__rO()
    H_2O = spro.H_2()

    spru = self.__rU()
    H_2U = spru.H_2()
    return self.b_O/self.b*H_2O+(1-self.b_O/self.b)*H_2U