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

def test_hippedroof():
  # test according to annax A2.5
  assert(hippedroof(1, 4, 3.65, 8) == 1.1)

def test_mansardroof():
  # test according to annax A2.6
  assert(mansardroof(1.7, 1.7, 3.3, 3, 0.7) == 1.6)
  assert(mansardroof(1.7, 0.8, 2.5, 3, 1.5) == 1.5)

def test_upstreamsinglebuilding():
  # test according to appendix A1, tabular A3
  # Building 1
  assert(upstreamsinglebuilding(13.4, 17.9, 90, 11.5) == 18.2)
  # Building 2
  assert(upstreamsinglebuilding(8.9, 12.7, 84, 6.8) == 13)
  # Building 4
  # slide difference of 0.1 in comparison to tabular A3, might be
  # due to rounding error
  assert(upstreamsinglebuilding(12.1, 9.9, 52, 7.0) == 17.6)
  # Building 5
  # slide difference of 0.1 in comparison to tabular A3, might be
  # due to rounding error
  assert(upstreamsinglebuilding(15.6, 18.6, 76, 11.0) == 23.8)

def test_recirculationheightupstreambuilding():
  # test according to appendix A1, tabular A3
  # Building 1
  assert(recirculationheightupstreambuilding(11.5, 2.8, 10.4, 18.2, 17.4) == -5.8)
  # Building 5
  assert(recirculationheightupstreambuilding(11, 3.3, 10.4, 23.7, 16.5) == 0.3)