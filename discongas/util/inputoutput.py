def additiveterm(nominalheatoutput, ratedthermalinput):
  """
  Values for the additive term H_Ü to account for the turbulent shear layer of a recirculation one for appliances and boilers according to table 1

  :param nominalheatoutput: Nominal heat output (in kW):
  :param ratedthermalinput: Rated thermal input (in MW):

  :return: additive term H_Ü
  """

  if nominalheatoutput <= 400:
    return 0.5
  elif nominalheatoutput > 400 and ratedthermalinput < 1:
    return 1
  else:
    return 3