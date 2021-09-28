
def exposurezone(nominalheatoutput, solidfuel=True, thirtyfirstbimschv=False):
  """
  Radius of exposure zone.

  :param nominalheatoutput: nominal heat output (in kW):
  :param solidfuel: if True - solid fuel heating appliance otherwise liquid or gas burning appliance (Boolean):
  :param thirteefirstbimschv: appliance according to 31.BImSchV (Boolean):

  :return: horizontal recirculation zone length
  """
  if thirtyfirstbimschv:
    return 50
  else:
    if solidfuel:
      if nominalheatoutput <= 50:
        return 15
      elif nominalheatoutput >50 and nominalheatoutput <= 100:
        return 17
      elif nominalheatoutput >100 and nominalheatoutput <= 150: 
        return 19
      elif nominalheatoutput >150 and nominalheatoutput <= 200: 
        return 21
      elif nominalheatoutput >200 and nominalheatoutput <= 250: 
        return 23
      elif nominalheatoutput >250 and nominalheatoutput <= 300: 
        return 25
      elif nominalheatoutput >300 and nominalheatoutput <= 350: 
        return 27
      elif nominalheatoutput >350 and nominalheatoutput <= 400: 
        return 29
      elif nominalheatoutput >400 and nominalheatoutput <= 450: 
        return 31
      elif nominalheatoutput >450 and nominalheatoutput <= 500: 
        return 33
      elif nominalheatoutput >500 and nominalheatoutput <= 550: 
        return 35
      elif nominalheatoutput >550 and nominalheatoutput <= 600: 
        return 37
      elif nominalheatoutput >600 and nominalheatoutput <= 650: 
        return 39
      elif nominalheatoutput >650 and nominalheatoutput <= 700: 
        return 41
      elif nominalheatoutput >700 and nominalheatoutput <= 750: 
        return 43
      elif nominalheatoutput >750 and nominalheatoutput <= 800: 
        return 45
      elif nominalheatoutput >800 and nominalheatoutput <= 850: 
        return 47
      elif nominalheatoutput >850 and nominalheatoutput <= 900: 
        return 49
      else:
        return 50
    else:
      if nominalheatoutput <= 50:
        return 8
      elif nominalheatoutput >50 and nominalheatoutput <= 100:
        return 9
      elif nominalheatoutput >100 and nominalheatoutput <= 150: 
        return 10
      elif nominalheatoutput >150 and nominalheatoutput <= 200: 
        return 11
      elif nominalheatoutput >200 and nominalheatoutput <= 250: 
        return 12
      elif nominalheatoutput >250 and nominalheatoutput <= 300: 
        return 13
      elif nominalheatoutput >300 and nominalheatoutput <= 350: 
        return 14
      elif nominalheatoutput >350 and nominalheatoutput <= 400: 
        return 15
      elif nominalheatoutput >400 and nominalheatoutput <= 450: 
        return 16
      elif nominalheatoutput >450 and nominalheatoutput <= 500: 
        return 17
      elif nominalheatoutput >500 and nominalheatoutput <= 550: 
        return 18
      elif nominalheatoutput >550 and nominalheatoutput <= 600: 
        return 19
      elif nominalheatoutput >600 and nominalheatoutput <= 650: 
        return 20
      elif nominalheatoutput >650 and nominalheatoutput <= 700: 
        return 21
      elif nominalheatoutput >700 and nominalheatoutput <= 750: 
        return 22
      elif nominalheatoutput >750 and nominalheatoutput <= 800: 
        return 23
      elif nominalheatoutput >800 and nominalheatoutput <= 850: 
        return 24
      elif nominalheatoutput >850 and nominalheatoutput <= 900: 
        return 25
      elif nominalheatoutput >900 and nominalheatoutput <= 950: 
        return 26
      elif nominalheatoutput >950 and nominalheatoutput <= 1000: 
        return 27
      else:
        return 28