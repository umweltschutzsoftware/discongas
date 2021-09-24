from discongas.undisturbedremoval import *

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

def test_flatroofs():
  # test according to annax A2.1
  # only the rooftop building is considered
  assert(flatroofs(4, 4) == 1.1)