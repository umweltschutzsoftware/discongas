import math
from discongas.util.inputoutput import *
from discongas.util.roof import *

def symmetricpitchedroof(a, H_Dach, dridge, nominalheatoutput=400, ratedthermalinput=1, flatroof=False):
  """
  Outlet height for symmetric pitched roofs.

  :param a: horizontal distance beween the centre of the outlet cross-section and the ridge (in m):
  :param H_Dach: the buildings actual roof height (in m):
  :param dridge: Horizontal distance from the gable to the ridge on the side where the outlet is placed (in m):
  :param nominalheatoutput: Nominal heat output (in kW):
  :param ratedthermalinput: Rated thermal input (in MW):
  :param flatroof: Indicates wether a flat roof should be considered (Boolean):

  :return: height H_A1
  """
  if (not flatroof):
    alpha = roofangle(H_Dach, dridge)
  else:
    alpha = 0

  gamma, f = roofpitchcorrection(alpha)

  if (alpha >= 20):
    H_1 = a * math.tan((alpha-gamma)*math.pi/180)
    H_2 = f * H_Dach
  else:
    if (dridge == 0):
      raise TypeError("The width b needs to be defined if roof angle alpha is less than 20 degree.")
    f = alpha/20*0.85
    H_1 = (a+dridge)*math.tan(20*math.pi/180)-H_Dach
    H_2 = (1+f)*dridge*math.tan(20*math.pi/180)-H_Dach

  H_S1 = min(H_1, H_2)
  H_Ü = additiveterm(nominalheatoutput, ratedthermalinput)

  return round(H_S1 + H_Ü, 1)

def flatroof(H_First, b, nominalheatoutput=400, ratedthermalinput=1):
  """
  Outlet height for flat roofs.

  :param H_First: the buildings ridge height (in m):
  :param b: Width of the buildings gable end or narrow side of the building for flat roofs (in m):
  :param nominalheatoutput: Nominal heat output (in kW):
  :param ratedthermalinput: Rated thermal input (in MW):

  :return: height H_A1
  """
  H_A1 = symmetricpitchedroof(0, 0, b, nominalheatoutput, ratedthermalinput, True)
  H_Ü = additiveterm(nominalheatoutput, ratedthermalinput)
  H_A1F = round(1.3*((H_First**2)**(1./3.))+H_Ü,1)
  return min(H_A1, H_A1F)

def singlepitchroof(a, H_Dach, b, nominalheatoutput=400, ratedthermalinput=1):
  """
  Outlet height for single pitch roofs.

  :param H_Dach: the buildings actual roof height (in m):
  :param b: Width of the buildings gable (in m):
  :param nominalheatoutput: Nominal heat output (in kW):
  :param ratedthermalinput: Rated thermal input (in MW):

  :return: height H_A1
  """
  alpha = roofangle(H_Dach, b)
  if (alpha >= 20):
    c = 0
  else: 
    c=(b/2-a)*(1-alpha/20)

  H_1 = (a+c)*math.tan(20*math.pi/180)
  H_2 = b/2*math.tan(20*math.pi/180)

  H_S1 = min(H_1, H_2)
  H_Ü = additiveterm(nominalheatoutput, ratedthermalinput)

  return round(H_S1 + H_Ü, 1)

def asymmetricpitchedroof(a, H_Dach, dridge, b_1, nominalheatoutput=400, ratedthermalinput=1):
  """
  Outlet height for asymmetric pitched roofs.

  :param H_Dach: the buildings actual roof height (in m):
  :param dridge: Horizontal distance from the gable to the ridge on the side where the outlet is placed (in m):
  :param b_1: Width of the gable from the gable to the ridge on the opposite side of the outlet (in m):
  :param nominalheatoutput: Nominal heat output (in kW):
  :param ratedthermalinput: Rated thermal input (in MW):

  :return: height H_A1
  """
  alpha_1 = roofangle(H_Dach, b_1)
  alpha_2 = roofangle(H_Dach, dridge)
  b = b_1 + dridge
  
  if alpha_1 < 75 and alpha_2 < 75:
    return symmetricpitchedroof(a, H_Dach, b_1, nominalheatoutput, ratedthermalinput, False)
  else:
    return singlepitchroof(a, H_Dach, b, nominalheatoutput, ratedthermalinput)