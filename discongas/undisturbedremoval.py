import math
from discongas.util.inputoutput import *
from discongas.util.roof import *

def roofpitchcorrection(alpha):
  """
  Calculate the roof pitch correction gamma and factor f as a function of the roof pitch alpha.

  :param alpha: roof pitch:

  :return: a tuple (gamma, f)
  """
  if alpha < 20:
    return (0, 0)
  if alpha >= 20 and alpha <= 30:
    gamma = 0

    # multiplier to interpolate
    m = (alpha-20)/10

    f = round(0.85 - 0.15 * m, 2)

  elif alpha > 30 and alpha <= 45:
    # multiplier to interpolate
    m = (alpha-30)/15

    gamma = round(10 * m, 2)
    f = round(0.7 - 0.2 * m, 2)

  elif alpha > 45 and alpha < 60:
    # multiplier to interpolate
    m = (alpha-45)/15

    gamma = round(10 + 10 * m, 2)
    f = round(0.5 - 0.05 * m, 2)

  else:
    gamma = 20
    f = 0.45
    
  return (gamma, f)

def symmetricpitchedroofs(a, H_Dach, b, nominalheatoutput=400, ratedthermalinput=1):
  """
  Outlet height for symmetric pitched roofs.

  :param a: horizontal distance beween the centre of the outlet cross-section and the ridge (in m):
  :param H_Dach: the buildings actual roof height (in m):
  :param b: Width of the buildings gable end or narrow side of the building for flat roofs (in m):
  :param nominalheatoutput: Nominal heat output (in kW):
  :param ratedthermalinput: Rated thermal input (in MW):

  :return: height H_A1
  """
  alpha = roofangle(H_Dach, b/2)

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
  