import math
from discongas.util.inputoutput import *
from discongas.util.roof import *

def symmetricpitchedroofs(a, H_Dach, b, nominalheatoutput=400, ratedthermalinput=1, flatroof=False):
  """
  Outlet height for symmetric pitched roofs.

  :param a: horizontal distance beween the centre of the outlet cross-section and the ridge (in m):
  :param H_Dach: the buildings actual roof height (in m):
  :param b: Width of the buildings gable end or narrow side of the building for flat roofs (in m):
  :param nominalheatoutput: Nominal heat output (in kW):
  :param ratedthermalinput: Rated thermal input (in MW):
  :param flatroof: Indicates wether a flat roof should be considered (Boolean):

  :return: height H_A1
  """
  if (not flatroof):
    alpha = roofangle(H_Dach, b/2)
  else:
    alpha = 0

  gamma, f = roofpitchcorrection(alpha)

  if (alpha >= 20):
    H_1 = a * math.tan((alpha-gamma)*math.pi/180)
    H_2 = f * H_Dach
  else:
    if (b == 0):
      raise TypeError("The width b needs to be defined if roof angle alpha is less than 20 degree.")
    f = alpha/20*0.85
    H_1 = (a+b/2)*math.tan(20*math.pi/180)-H_Dach
    H_2 = (1+f)*b/2*math.tan(20*math.pi/180)-H_Dach

  H_S1 = min(H_1, H_2)
  H_Ü = additiveterm(nominalheatoutput, ratedthermalinput)

  return round(H_S1 + H_Ü,1)

def flatroofs(H_First, b, nominalheatoutput=400, ratedthermalinput=1):
  """
  Outlet height for flat roofs.

  :param H_First: the buildings ridge height (in m):
  :param b: Width of the buildings gable end or narrow side of the building for flat roofs (in m):
  :param nominalheatoutput: Nominal heat output (in kW):
  :param ratedthermalinput: Rated thermal input (in MW):

  :return: height H_A1
  """
  H_A1 = symmetricpitchedroofs(0, 0, b, nominalheatoutput, ratedthermalinput, True)
  H_Ü = additiveterm(nominalheatoutput, ratedthermalinput)
  H_A1F = round(1.3*((H_First**2)**(1./3.))+H_Ü,1)
  return min(H_A1, H_A1F)