from discongas.util.roof import *

def test_roofangle():
  # test according to annax table A1
  # house 1
  assert(roofangle(4, 6.7) == 31)
  # house 2
  assert(roofangle(3.4, 6.35) == 28)
  # house 3
  assert(roofangle(3.7, 5.65) == 33)
  # house 4
  assert(roofangle(3.6, 4.95) == 36)
  # house 5
  assert(roofangle(4.9, 7.8) == 32)

  # less than 20 degree
  assert(roofangle(2.45, 7.8) == 17)