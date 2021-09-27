from discongas.undisturbedremoval import *

def test_symmetricpitchedroof():
  # test according to annax A1.2
  # X1
  assert(symmetricpitchedroof(0, 3.7, 5.65) == 0.4)
  # X2 
  assert(symmetricpitchedroof(5.7, 3.7, 5.65) == 2.8)
  # X3 
  assert(symmetricpitchedroof(0, 3.7, 5.65) == 0.4)

  # test with a roof angle == 20
  assert(symmetricpitchedroof(0, 3.7, 5.65) == 0.4)

  # test with a roof angle < 20
  assert(symmetricpitchedroof(0, 2.45, 7.8) == 0.8)

def test_flatroof():
  # test according to annax A2.1
  # only the rooftop building is considered
  assert(flatroof(4, 2) == 1.1)

def test_singlepitchroof():
  # test according to annax A2.3
  assert(singlepitchroof(0, 3.7, 8)==0.4)
  assert(singlepitchroof(4, 3.7, 8)==1.9)
  assert(singlepitchroof(8, 3.7, 8)==1.9)

  assert(singlepitchroof(0, 2.5, 8) == 0.6)
  assert(singlepitchroof(4, 2.5, 8) == 1.9)
  assert(singlepitchroof(8, 2.5, 8) == 1.9)

def test_asymmetricpitchedroof():
  # test according to annax A2.3
  assert(asymmetricpitchedroof(1.9, 3, 6, 2) == 1.8)
  assert(asymmetricpitchedroof(0.6, 3, 2, 6) == 0.7)

def test_sawtoothroof():
  # test according to annax A2.4
  assert(sawtoothroof(7.5, 9.75) == 3.9)