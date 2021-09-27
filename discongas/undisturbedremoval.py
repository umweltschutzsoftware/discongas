import math
from discongas.util.inputoutput import *
from discongas.util.roof import *

def outletheight(alpha, gamma, a, f, H_Dach, dridge):
  if (alpha >= 20):
    H_1 = a * math.tan((alpha-gamma)*math.pi/180)
    H_2 = f * H_Dach
  else:
    if (dridge == 0):
      raise TypeError("The width b needs to be defined if roof angle alpha is less than 20 degree.")
    f = alpha/20*0.85
    H_1 = (a+dridge)*math.tan(20*math.pi/180)-H_Dach
    H_2 = (1+f)*dridge*math.tan(20*math.pi/180)-H_Dach
  return H_1, H_2

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

  H_1, H_2 = outletheight(alpha, gamma, a, f, H_Dach, dridge)

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

def sawtoothroof(H_First, b, nominalheatoutput=400, ratedthermalinput=100):
  """
  Outlet height for saw-tooth roofs.

  :param H_Dach: the buildings actual roof height (in m):
  :param b: Width of the buildings gable (in m):
  :param nominalheatoutput: Nominal heat output (in kW):
  :param ratedthermalinput: Rated thermal input (in MW):

  :return: height H_A1
  """
  return flatroof(H_First, b, nominalheatoutput, ratedthermalinput)

def hippedroof(a, H_Dach, dridge, depth, nominalheatoutput=400, ratedthermalinput=1):
  """
  Outlet height for hipped roofs.

  :param a: horizontal distance beween the centre of the outlet cross-section and the ridge (in m):
  :param H_Dach: the buildings actual roof height (in m):
  :param dridge: Horizontal distance from the gable to the ridge on the side where the outlet is placed (in m):
  :param depth: Depth of the house (in m):
  :param nominalheatoutput: Nominal heat output (in kW):
  :param ratedthermalinput: Rated thermal input (in MW):

  :return: height H_A1
  """
  H_A1 = symmetricpitchedroof(a, H_Dach, dridge, nominalheatoutput, ratedthermalinput)
  H_Ü = additiveterm(nominalheatoutput, ratedthermalinput)
  H_S1 = H_A1 - H_Ü
  if depth <= dridge*2 <= depth*1.2:
    return round(H_S1*0.4+H_Ü)
  return H_A1

def mansardroof(a, H_DachO, dridge_O, H_DachU, dridge_U, nominalheatoutput=400, ratedthermalinput=1):
  """
  Outlet height for mansard roofs.

  :param a: horizontal distance beween the centre of the outlet cross-section and the ridge (in m):
  :param H_DachO: the height of the upper roof part (in m):
  :param dridge_O: Horizontal distance from the gable of the upper roof part to the ridge on the side where the outlet is placed (in m):
  :param H_DachU: the height of the lower roof part (in m):
  :param dridge_U: Horizontal distance from the gable of the lower roof part to the gable of the upper roof part on the side where the outlet is placed (in m):
  :param nominalheatoutput: Nominal heat output (in kW):
  :param ratedthermalinput: Rated thermal input (in MW):

  :return: height H_A1
  """
  dridge = dridge_U + dridge_O

  alpha_O = roofangle(H_DachO, dridge_O)
  gamma_O, f_O = roofpitchcorrection(alpha_O)
  H_DachalphaO = dridge * math.tan(math.pi*alpha_O/180)
  H_1O, H_2O = outletheight(alpha_O, gamma_O, a, f_O, H_DachalphaO, dridge)

  alpha_U = 90-roofangle(dridge_U, H_DachU)
  gamma_U, f_U = roofpitchcorrection(alpha_U)
  H_DachalphaU = dridge * math.tan(math.pi*alpha_U/180)
  H_1U, H_2U = outletheight(alpha_U, gamma_U, a, f_U, H_DachalphaU, dridge)

  H_1 = dridge_O/dridge * H_1O + (1-dridge_O/dridge) * H_1U
  H_2 = dridge_O/dridge * H_2O + (1-dridge_O/dridge) * H_2U

  H_S1 = min(H_1, H_2)
  H_Ü = additiveterm(nominalheatoutput, ratedthermalinput)

  return round(H_S1 + H_Ü, 1)

def upstreamsinglebuilding(l_V, b_V, beta, H_First):
  """
  Reciruculation zone of a single building.

  :param l_V: length of the upstream building (in m):
  :param b_V: width of the upstream building (in m):
  :param beta: horizontal angle between an upstream building an the direction of the exhaust gas discharge system (in m):
  :param H_First: ridge height of the upstream building (in m):

  :return: horizontal recirculation zone length
  """
  l_eff = l_V * math.sin(beta * math.pi / 180) + b_V * math.cos(beta * math.pi / 180)
  l_rz = (1.75*l_eff)/(1+0.25*l_eff/H_First)
  return round(l_rz,1)

def contiguousbuilding(H_First):
  """
  Reciruculation zone of contiguous buildings.

  :param H_First: ridge height of the upstream building (in m):

  :return: horizontal recirculation zone length
  """
  return round(6*H_First, 1)