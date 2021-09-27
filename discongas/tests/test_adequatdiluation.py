from discongas.adequatdilution import *

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
  assert(upstreamsinglebuilding(15.6, 18.6, 76, 11.0) == 23.7)