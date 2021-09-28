from discongas.adequatdilution import *

def test_exposurezone():
  # test according to annax A1.3.1
  assert(exposurezone(15) == 15)

  # test 31. BImSchV
  assert(exposurezone(30, thirtyfirstbimschv=True) == 50)

  # liquid
  assert(exposurezone(456, solidfuel=False) == 17)

def test_referencelevel():
  # test according to annax A1.3.2
  assert(referencelevel(15, 8.6, 10.4) == -0.8)