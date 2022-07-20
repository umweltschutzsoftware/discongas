from discongas.outletheight import *

def test_heightbyundisturbedremoval():
  # test according to A1.2
  b3 = SymmetricPitchedRoof("b3", alpha=33, H_First=10.4, H_Dach=3.7, b=11.3, l=16.3, h=0)

  b1 = SymmetricPitchedRoof("b1", alpha=31, H_First=11.5, H_Dach=4, b=17.9, l=13.4, h=-2.1)
  b2 = SymmetricPitchedRoof("b2", alpha=28, H_First=6.8, H_Dach=3.4, b=12.7, l=8.9, h=0)
  b4 = SymmetricPitchedRoof("b4", alpha=36, H_First=7, H_Dach=3.6, b=9.9, l=15.6, h=0)
  b5 = SymmetricPitchedRoof("b5", alpha=32, H_First=11, H_Dach=4.9, b=18.6, l=15.6, h=1.7)

  # X1
  m = Model(0, b3)
  m.add_upstreamroof(beta=90, l_A=17.4, upstreamroof=b1)
  m.add_upstreamroof(beta=84, l_A=24.4, upstreamroof=b2)
  m.add_upstreamroof(beta=52, l_A=37.6, upstreamroof=b4)
  m.add_upstreamroof(beta=76, l_A=16.5, upstreamroof=b5)
  assert(m.heightbyundisturbedremoval() == 2.0)

  # X2
  m = Model(5.7, b3)
  m.add_upstreamroof(beta=78, l_A=17.7, upstreamroof=b1)
  m.add_upstreamroof(beta=81, l_A=18.8, upstreamroof=b2)
  m.add_upstreamroof(beta=48, l_A=32.4, upstreamroof=b4)
  m.add_upstreamroof(beta=87, l_A=19.2, upstreamroof=b5)
  assert(m.heightbyundisturbedremoval() == 2.8)

  # X3
  m = Model(0, b3)
  m.add_upstreamroof(beta=90, l_A=25.4, upstreamroof=b1)
  m.add_upstreamroof(beta=68, l_A=26.2, upstreamroof=b2)
  m.add_upstreamroof(beta=62, l_A=33.9, upstreamroof=b4)
  m.add_upstreamroof(beta=84, l_A=9.2, upstreamroof=b5)
  assert(m.heightbyundisturbedremoval() == 4.7)

def test_heightbyadequatedilution():
  # test according to A1.3
  b3 = SymmetricPitchedRoof("b3", alpha=33, H_First=10.4, H_Dach=3.7, b=11.3, l=16.3, h=0, nominalheatoutput=15)

  b1 = SymmetricPitchedRoof("b1", alpha=31, H_First=11.5, H_Dach=4, b=17.9, l=13.4, h=-2.1)
  b2 = SymmetricPitchedRoof("b2", alpha=28, H_First=6.8, H_Dach=3.4, b=12.7, l=8.9, h=0)
  b4 = SymmetricPitchedRoof("b4", alpha=36, H_First=7, H_Dach=3.6, b=9.9, l=15.6, h=0)
  b5 = SymmetricPitchedRoof("b5", alpha=32, H_First=11, H_Dach=4.9, b=18.6, l=15.6, h=1.7)

  # X3
  m = Model(0, b3)
  m.add_upstreamroof(beta=90, l_A=25.4, upstreamroof=b1)
  m.add_upstreamroof(beta=68, l_A=26.2, upstreamroof=b2)
  m.add_upstreamroof(beta=62, l_A=33.9, upstreamroof=b4)
  m.add_upstreamroof(beta=84, l_A=9.2, upstreamroof=b5)

  m.add_referencelevel(H_F=8.6, upstreamroof=b5)

  assert(m.heightbyadequatedilution() == 0.9)

def test_height():
  # test according to A1.4
  # no terrain
  b3 = SymmetricPitchedRoof("b3", alpha=33, H_First=10.4, H_Dach=3.7, b=11.3, l=16.3, h=0)

  b1 = SymmetricPitchedRoof("b1", alpha=31, H_First=11.5, H_Dach=4, b=17.9, l=13.4, h=0)
  b2 = SymmetricPitchedRoof("b2", alpha=28, H_First=6.8, H_Dach=3.4, b=12.7, l=8.9, h=0)
  b4 = SymmetricPitchedRoof("b4", alpha=36, H_First=7, H_Dach=3.6, b=9.9, l=15.6, h=0)
  b5 = SymmetricPitchedRoof("b5", alpha=32, H_First=11, H_Dach=4.9, b=18.6, l=15.6, h=0)

  # X1
  m = Model(0, b3)
  m.add_upstreamroof(beta=90, l_A=17.4, upstreamroof=b1)
  m.add_upstreamroof(beta=84, l_A=24.4, upstreamroof=b2)
  m.add_upstreamroof(beta=52, l_A=37.6, upstreamroof=b4)
  m.add_upstreamroof(beta=76, l_A=16.5, upstreamroof=b5)
  assert(m.height() == 0.4)

  # X2
  m = Model(5.7, b3)
  m.add_upstreamroof(beta=78, l_A=17.7, upstreamroof=b1)
  m.add_upstreamroof(beta=81, l_A=18.8, upstreamroof=b2)
  m.add_upstreamroof(beta=48, l_A=32.4, upstreamroof=b4)
  m.add_upstreamroof(beta=87, l_A=19.2, upstreamroof=b5)
  assert(m.height() == 2.8)

  # X3
  m = Model(0, b3)
  m.add_upstreamroof(beta=90, l_A=25.4, upstreamroof=b1)
  m.add_upstreamroof(beta=68, l_A=26.2, upstreamroof=b2)
  m.add_upstreamroof(beta=62, l_A=33.9, upstreamroof=b4)
  m.add_upstreamroof(beta=84, l_A=9.2, upstreamroof=b5)
  m.add_referencelevel(H_F=8.6, upstreamroof=b5)
  assert(m.height() == 3.0)

  # with terrain
  b3 = SymmetricPitchedRoof("b3", alpha=33, H_First=10.4, H_Dach=3.7, b=11.3, l=16.3, h=0)

  b1 = SymmetricPitchedRoof("b1", alpha=31, H_First=11.5, H_Dach=4, b=17.9, l=13.4, h=-2.1)
  b2 = SymmetricPitchedRoof("b2", alpha=28, H_First=6.8, H_Dach=3.4, b=12.7, l=8.9, h=0)
  b4 = SymmetricPitchedRoof("b4", alpha=36, H_First=7, H_Dach=3.6, b=9.9, l=15.6, h=0)
  b5 = SymmetricPitchedRoof("b5", alpha=32, H_First=11, H_Dach=4.9, b=18.6, l=15.6, h=1.7)

  # X1
  m = Model(0, b3)
  m.add_upstreamroof(beta=90, l_A=17.4, upstreamroof=b1)
  m.add_upstreamroof(beta=84, l_A=24.4, upstreamroof=b2)
  m.add_upstreamroof(beta=52, l_A=37.6, upstreamroof=b4)
  m.add_upstreamroof(beta=76, l_A=16.5, upstreamroof=b5)
  assert(m.height() == 2.0)

  # X2
  m = Model(5.7, b3)
  m.add_upstreamroof(beta=78, l_A=17.7, upstreamroof=b1)
  m.add_upstreamroof(beta=81, l_A=18.8, upstreamroof=b2)
  m.add_upstreamroof(beta=48, l_A=32.4, upstreamroof=b4)
  m.add_upstreamroof(beta=87, l_A=19.2, upstreamroof=b5)
  assert(m.height() == 2.8)

  # X3
  m = Model(0, b3)
  m.add_upstreamroof(beta=90, l_A=25.4, upstreamroof=b1)
  m.add_upstreamroof(beta=68, l_A=26.2, upstreamroof=b2)
  m.add_upstreamroof(beta=62, l_A=33.9, upstreamroof=b4)
  m.add_upstreamroof(beta=84, l_A=9.2, upstreamroof=b5)
  m.add_referencelevel(H_F=8.6, upstreamroof=b5)
  assert(m.height() == 4.7)

def test_output():
  b3 = SymmetricPitchedRoof("b3", alpha=33, H_First=10.4, H_Dach=3.7, b=11.3, l=16.3, h=0)

  b1 = SymmetricPitchedRoof("b1", alpha=31, H_First=11.5, H_Dach=4, b=17.9, l=13.4, h=-2.1)
  b2 = SymmetricPitchedRoof("b2", alpha=28, H_First=6.8, H_Dach=3.4, b=12.7, l=8.9, h=0)
  b4 = SymmetricPitchedRoof("b4", alpha=36, H_First=7, H_Dach=3.6, b=9.9, l=15.6, h=0)
  b5 = SymmetricPitchedRoof("b5", alpha=32, H_First=11, H_Dach=4.9, b=18.6, l=15.6, h=1.7)

  m = Model(0, b3)
  m.add_upstreamroof(beta=90, l_A=25.4, upstreamroof=b1)
  m.add_upstreamroof(beta=68, l_A=26.2, upstreamroof=b2)
  m.add_upstreamroof(beta=62, l_A=33.9, upstreamroof=b4)
  m.add_upstreamroof(beta=84, l_A=9.2, upstreamroof=b5)
  m.add_referencelevel(H_F=8.6, upstreamroof=b5)

  d = m.height_with_dict()
  assert(d[0] == 4.7)
  assert(d[1] == 'UR')
  assert(d[2] == 'b5')

  # check source roof
  sr = d[3]['b3']
  assert('A' in sr.keys())
  assert('Beta' not in sr.keys())

  # check upstream roofs
  for k in d[3].keys():
    if k == 'b3':
      continue
    assert('Beta' in d[3][k].keys())
    assert('L_A' in d[3][k].keys())

  # H_F only is defined for house 'b5'
  assert('H_F' in d[3]['b5'].keys())
  assert(d[3]['b5']['H_F'] == 8.6)
  
  # Check if result is set
  assert(d[3]['b5']['H_A2T'] == 4.7)

def test_fromcsv():
  testfilepath = 'discongas/tests/testfiles/parameter.csv'
  m = Model.from_csv(testfilepath)
  assert(m.height() == 1.8)