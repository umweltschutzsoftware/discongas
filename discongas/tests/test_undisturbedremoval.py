from discongas.undisturbedremoval import *

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

def test_symmetricpitchedroofs():
  # test according to annax A1.2
  # X1
  assert(symmetricpitchedroofs(0, 3.7, 11.3) == 0.4)
  # X2 
  assert(symmetricpitchedroofs(5.7, 3.7, 11.3) == 2.8)
  # X3 
  assert(symmetricpitchedroofs(0, 3.7, 11.3) == 0.4)

  # test with a roof angle == 20
  assert(symmetricpitchedroofs(0, 3.7, 11.3) == 0.4)

  # test with a roof angle < 20
  assert(symmetricpitchedroofs(0, 2.45, 15.6) == 0.8)