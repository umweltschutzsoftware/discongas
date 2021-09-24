from discongas.util.roof import *

def test_roofpitchcorrection():
  # test of exact values according to table 2
  assert(roofpitchcorrection(20) == (0, 0.85))
  assert(roofpitchcorrection(30) == (0, 0.70))
  assert(roofpitchcorrection(45) == (10, 0.50))
  assert(roofpitchcorrection(60) == (20, 0.45))

  # test of values less than 20 or greater than 60
  assert(roofpitchcorrection(19) == (0, 0))
  assert(roofpitchcorrection(61) == (20, 0.45))

  # test of interpolation 
  assert(roofpitchcorrection(21) == (0, 0.83))
  assert(roofpitchcorrection(37.5) == (5, 0.6))
  assert(roofpitchcorrection(50) == (13.33, 0.48))

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