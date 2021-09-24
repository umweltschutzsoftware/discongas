import math

def roofangle(H_Dach, dridge):
  """
  Angle alpha of a roof. 

  :param H_Dach: the buildings actuial roof height (in m):
  :param dridge: Horizontal distance from the gable to the ridge (in m):

  :return: roof angle alpha
  """
  return round(math.tanh(H_Dach/dridge)*180/math.pi,0)
