from discongas.adequatdilution import *

def test_exposurezone():
  # test according to annax A1.3.1
  assert(exposurezone(15) == 15)

  # test 31. BImSchV
  assert(exposurezone(30, thirtyfirstbimschv=True) == 50)

  # liquid
  assert(exposurezone(456, solidfuel=False) == 17)