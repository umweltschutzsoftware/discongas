import math

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

def roofangle(H_Dach, dridge):
  """
  Angle alpha of a roof. 

  :param H_Dach: the buildings actuial roof height (in m):
  :param dridge: Horizontal distance from the gable to the ridge (in m):

  :return: roof angle alpha
  """
  return round(math.tanh(H_Dach/dridge)*180/math.pi,0)
