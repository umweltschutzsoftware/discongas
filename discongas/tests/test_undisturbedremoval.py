from discongas.undisturbedremoval import *

def test_symmetricpitchedroofs():
  # test according to annax A1.2
  # X1
  assert(symmetricpitchedroofs(0, 3.7, 5.65) == 0.4)
  # X2 
  assert(symmetricpitchedroofs(5.7, 3.7, 5.65) == 2.8)
  # X3 
  assert(symmetricpitchedroofs(0, 3.7, 5.65) == 0.4)

  # test with a roof angle == 20
  assert(symmetricpitchedroofs(0, 3.7, 5.65) == 0.4)

  # test with a roof angle < 20
  assert(symmetricpitchedroofs(0, 2.45, 7.8) == 0.8)

def test_flatroofs():
  # test according to annax A2.1
  # only the rooftop building is considered
  assert(flatroofs(4, 2) == 1.1)

def test_singlepitchroof():
  # test according to annax A2.3
  assert(singlepitchroof(0, 3.7, 8)==0.4)
  assert(singlepitchroof(4, 3.7, 8)==1.9)
  assert(singlepitchroof(8, 3.7, 8)==1.9)

  assert(singlepitchroof(0, 2.5, 8) == 0.6)
  assert(singlepitchroof(4, 2.5, 8) == 1.9)
  assert(singlepitchroof(8, 2.5, 8) == 1.9)