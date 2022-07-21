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
  assert(d['Result']['Source'] == 'Undisturbed Removal')
  assert(d['Result']['Height'] == 4.7)

  assert(d['Adequate Dilution']['Source'] == 'b5')
  assert(d['Adequate Dilution']['Height'] == 3.9)

  assert(d['Undisturbed Removal']['Source'] == 'b5')
  assert(d['Undisturbed Removal']['Height'] == 4.7)

  assert(d['Number of upstream roofs'] == 4)

  sourceroofid = d['Source Roof']
  assert(sourceroofid == 'b3')

  assert(len(d['Data']) == 5)

  # check upstream roofs
  dd = d['Data']
  for k in dd.keys():
    assert('Alpha' in dd[k].keys())
    assert('H_First' in dd[k].keys())
    assert('H_Dach' in dd[k].keys())
    assert('A' in dd[k].keys())
    assert('L_A' in dd[k].keys())
    assert('Beta' in dd[k].keys())
    assert('L_RZ' in dd[k].keys())
    assert('H_A1' in dd[k].keys())
    assert('H_A2' in dd[k].keys())
    assert('H_A2T' in dd[k].keys())
    assert('H_E1' in dd[k].keys())
    assert('H_E2' in dd[k].keys())
    assert('H_E2T' in dd[k].keys())
    assert('H_F' in dd[k].keys())
    assert('Hoehe' in dd[k].keys())

def test_outputcontent():
  sr = FlatRoof('G1', 0, 6.5, 0, 7.5, 10.7, 225.7, nominalheatoutput=15)
  m = Model(0, sr)
  
  ur3 = FlatRoof('G3', 0, 8, 0, 12, 12, 230.9, address='My Street 13')
  ur8 = FlatRoof('G8', 0, 6.5, 0, 7.5, 10.7, 222.1)

  m.add_upstreamroof(77.7, 16.3, ur3)
  m.add_upstreamroof(88.4, 6.5, ur8)

  m.add_referencelevel(6, ur8)

  d = m.height_with_dict()

  # Result is based on UR given by G3
  assert(d['Result']['Source'] == 'Undisturbed Removal')
  assert(d['Undisturbed Removal']['Source'] == 'G3')
  
  # Adequate Dilution is only verified for G8
  assert(d['Adequate Dilution']['Source'] == 'G8')

  # Three roofs
  assert(len(d['Data']) == 3)

  # Parameters for G1
  assert(d['Data']['G1']['Name'] == 'G1')
  assert(d['Data']['G1']['A'] == 0)
  assert(d['Data']['G1']['L'] == 10.7)
  assert(d['Data']['G1']['B'] == 7.5)
  assert(d['Data']['G1']['H_First'] == 6.5)
  assert(d['Data']['G1']['H_Dach'] == 0)
  assert(d['Data']['G1']['H_A1'] == 1.8)
  assert(d['Data']['G1']['E_Zone'] == 15)
  assert(d['Data']['G1']['Type'] == 'Flachdach')
  assert(d['Data']['G1']['Hoehe'] == 225.7)

  # Parameters for G3
  assert(d['Data']['G3']['L_RZ'] == 17.3)
  assert(d['Data']['G3']['H_A2'] == 0)
  assert(d['Data']['G3']['H_A2T'] == 2.5)
  assert(d['Data']['G3']['Address'] == 'My Street 13')

# Parameters for G8
  assert(d['Data']['G8']['H_E2'] == 0)
  assert(d['Data']['G8']['H_E2T'] == -3.1)
  assert(d['Data']['G8']['H_F'] == 6)
  

def test_fromcsv():
  testfilepath = 'discongas/tests/testfiles/parameter.csv'
  m = Model.from_csv(testfilepath)
  assert(m.height() == 1.8)