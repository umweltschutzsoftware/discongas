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
  assert(m.H_A() == 2.0)

  # X2
  m = Model(5.7, b3)
  m.add_upstreamroof(beta=78, l_A=17.7, upstreamroof=b1)
  m.add_upstreamroof(beta=81, l_A=18.8, upstreamroof=b2)
  m.add_upstreamroof(beta=48, l_A=32.4, upstreamroof=b4)
  m.add_upstreamroof(beta=87, l_A=19.2, upstreamroof=b5)
  assert(m.H_A() == 2.8)

  # X3
  m = Model(0, b3)
  m.add_upstreamroof(beta=90, l_A=25.4, upstreamroof=b1)
  m.add_upstreamroof(beta=68, l_A=26.2, upstreamroof=b2)
  m.add_upstreamroof(beta=62, l_A=33.9, upstreamroof=b4)
  m.add_upstreamroof(beta=84, l_A=9.2, upstreamroof=b5)
  assert(m.H_A() == 4.7)

def test_heightbyadequatedilution():
  # test according to A1.3
  b3 = SymmetricPitchedRoof("b3", alpha=33, H_First=10.4, H_Dach=3.7, b=11.3, l=16.3, h=0)

  b1 = SymmetricPitchedRoof("b1", alpha=31, H_First=11.5, H_Dach=4, b=17.9, l=13.4, h=-2.1)
  b2 = SymmetricPitchedRoof("b2", alpha=28, H_First=6.8, H_Dach=3.4, b=12.7, l=8.9, h=0)
  b4 = SymmetricPitchedRoof("b4", alpha=36, H_First=7, H_Dach=3.6, b=9.9, l=15.6, h=0)
  b5 = SymmetricPitchedRoof("b5", alpha=32, H_First=11, H_Dach=4.9, b=18.6, l=15.6, h=1.7)

  # X3
  m = Model(0, b3, nominalheatoutput=15)
  m.add_upstreamroof(beta=90, l_A=25.4, upstreamroof=b1)
  m.add_upstreamroof(beta=68, l_A=26.2, upstreamroof=b2)
  m.add_upstreamroof(beta=62, l_A=33.9, upstreamroof=b4)
  m.add_upstreamroof(beta=84, l_A=9.2, upstreamroof=b5, H_F=8.6)

  H_E = m.H_E()
  assert(m.H_B == 1)
  assert(m.H_E2_source.name == "b5")
  assert(m.H_E2_source.H_E2(8.6, 1, b3.H_First) == -0.8)
  assert(m.H_E2T_source.H_E2T(8.6, 1, b3.H_First, b3.h) == 0.9)
  assert(H_E == 0.9)

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
  m.add_upstreamroof(beta=84, l_A=9.2, upstreamroof=b5, H_F=8.6)
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
  m.add_upstreamroof(beta=84, l_A=9.2, upstreamroof=b5, H_F=8.6)
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
  m.add_upstreamroof(beta=84, l_A=9.2, upstreamroof=b5, H_F=8.6)

  height = m.height()
    
  assert(m.H_source.name == m.H_A_source.name)
  assert(height == 4.7)

  assert(m.H_E_source.name == "b5")
  assert(m.H_E() == 3.9)

  assert(m.H_A_source.name == "b5")
  assert(m.H_A() == 4.7)

  assert(len(m.upstreamroofs) == 4)

  assert(m.sourceroof.name == "b3")

def test_outputcontent():
  sr = FlatRoof('G1', 0, 6.5, 0, 7.5, 10.7, 225.7)
  m = Model(0, sr, nominalheatoutput=15)
  
  ur3 = FlatRoof('G3', 0, 8, 0, 12, 12, 230.9, address='My Street 13')
  ur8 = FlatRoof('G8', 0, 6.5, 0, 7.5, 10.7, 222.1)

  m.add_upstreamroof(77.7, 16.3, ur3)
  m.add_upstreamroof(88.4, 6.5, ur8, H_F=6)

  h = m.height()

  # Result is based on UR given by G3

  assert(m.H_source == m.H_A_source)
  assert(m.H_A_source.name == "G3")

  assert(m.H_E_source.name == "G1")

  assert(len(m.upstreamroofs) == 2)

  assert(m.sourceroof.name == "G1")
  assert(m.a == 0)
  assert(m.sourceroof.l == 10.7)
  assert(m.sourceroof.b == 7.5)
  assert(m.sourceroof.H_First == 6.5)
  assert(m.sourceroof.H_Dach == 0)
  assert(m.sourceroof.H_A1(m.a, m.H_U))
  assert(m.sourceroof.b == 7.5)
  assert(m.exposure_zone() == 15)
  assert(m.sourceroof.h == 225.7)
  assert(m.H_B == 1)
  assert(m.sourceroof.H_1(m.a) == 1.4, 1)
  assert(m.sourceroof.H_2() == 1.4, 1)

  # Parameters for G3
  for r in m.upstreamroofs:
    roof, beta, l_A, H_F = r
    if roof.name == "G3":
      assert(roof.L_RZ(beta) == 17.3) 
      assert(roof.H_A2(beta, l_A, m.sourceroof.H_First, m.H_U) <= 0)
      assert(roof.H_A2T(beta, l_A, m.sourceroof.H_First, m.H_U, m.sourceroof.h) == 2.5)
      assert(roof.address == 'My Street 13')
    elif roof.name == "G8":
      assert(roof.H_E2(H_F, m.H_B, m.sourceroof.H_First) == 0.5)
      assert(roof.H_E2T(H_F, m.H_B, m.sourceroof.H_First, m.sourceroof.h) == -3.1)
      assert(H_F == 6)

def test_heightdifference():
  sr = SymmetricPitchedRoof("G1",17.9, 4.74, 1.92, 11.9, 13.3, 281.48)

  ur = SymmetricPitchedRoof("G2", 18.4, 4.74, 3, 18, 14, 280.41)

  m = Model(3, sr)
  m.add_upstreamroof(73.4, 9.1, ur)

  assert(m.height() == 1.7)