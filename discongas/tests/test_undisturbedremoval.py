from discongas.undisturbedremoval import *

def test_symmetricpitchedroof():
  # test according to annax A1.2
  spr = SymmetricPitchedRoof(name="", alpha=33, H_First=10.4, H_Dach=3.7, b=11.3, l=16.3, h=0)
  # X1
  assert(spr.H_A1(0) == 0.4)
  # X2 
  assert(spr.H_A1(5.6) == 2.8)
  # X3 
  assert(spr.H_A1(0) == 0.4)

def test_flatroof():
  # test according to annax A2.1.3
  fr = FlatRoof(name="", alpha=0, H_First=8, H_Dach=0, b=15, l=28, h=0)
  assert(fr.H_A1(0) == 3.1)

def test_asymmetricpitchedroof():
  # test according to annax A.2.2
  # outlet on the flat side
  apr = AsymmetricPitchedRoof(name="", alpha=27, H_First=7, H_Dach=3, b=6, l=9, h=0)
  assert(apr.H_A1(0.6) == 0.7)
  # outlet on the steep side
  apr =  AsymmetricPitchedRoof(name="", alpha=56, H_First=7, H_Dach=3, b=2, l=9, h=0)
  assert(apr.H_A1(1.9) == 1.8)

def test_singlepithroof():
  # test according to annax A2.3
  spr = SinglePitchRoof(name="", alpha=25, H_First=7.7, H_Dach=3.7, b=8, l=12, h=0)
  assert(spr.H_A1(0) == 0.4)
  assert(spr.H_A1(4) == 1.9)
  assert(spr.H_A1(8) == 1.9)

  spr = SinglePitchRoof(name="", alpha=17, H_First=7.7, H_Dach=3.7, b=8, l=12, h=0)
  assert(spr.H_A1(0) == 0.6)
  assert(spr.H_A1(4) == 1.9)
  assert(spr.H_A1(8) == 1.9)

def test_sawtoothroof():
  # test according to annax A2.4
  str = SawToothRoof(name="", alpha=0, H_First=7.5, H_Dach=1.5, b=19.5, l=25.6, h=0)
  assert(str.H_A1(0) == 3.9)

def test_hippedroof():
  # test according to annax A2.5
  hr = HippedRoof(name="", alpha=48, H_First=7.5, H_Dach=4, b=7.3, l=8, h=0)
  assert(hr.H_A1(1) == 0.8)

  hr = HippedRoof(name="", alpha=48, H_First=7.5, H_Dach=4, b=7.3, l=9, h=0)
  assert(hr.H_A1(1) == 1.1)

def test_mansardroof():
  # test according to annax A2.6
  mr = MansardRoof(name="", alpha=77, H_First=10.7, H_Dach=4.7, b=8, l=12, b_O=6.6, alpha_O=27, h=0)
  assert(mr.H_A1(1.7) == 1.6)
  mr = MansardRoof(name="", alpha=63, H_First=10.7, H_Dach=4.7, b=8, l=12, b_O=5, alpha_O=18, h=0)
  assert(mr.H_A1(1.7) == 1.5)

def test_upstreamsinglebuilding():
  # test according to appendix A1, tabular A3
  # Building 1
  r = SymmetricPitchedRoof(name="", alpha=31, H_First=11.5, H_Dach=4, b=17.9, l=13.4, h=0)
  assert(r.L_RZ(beta=90) == 18.2)
  # Building 2
  r = SymmetricPitchedRoof(name="", alpha=28, H_First=6.8, H_Dach=3.4, b=12.7, l=8.9, h=0)
  assert(r.L_RZ(beta=84) == 13)
  # Building 4
  r = SymmetricPitchedRoof(name="", alpha=36, H_First=7, H_Dach=3.6, b=9.9, l=12.1, h=0)
  assert(r.L_RZ(beta=52) == 17.6)
  # Building 5
  r = SymmetricPitchedRoof(name="", alpha=32, H_First=11, H_Dach=4.9, b=18.6, l=15.6, h=0)
  assert(r.L_RZ(beta=76) == 23.8)

def test_recirculationheightupstreambuilding():
  # test according to appendix A1, tabular A3
  # Building 1
  r = SymmetricPitchedRoof(name="", alpha=31, H_First=11.5, H_Dach=4, b=17.9, l=13.4, h=0)
  assert(r.H_A2(beta=90, l_A=17.4, H_First=10.4, H_U=0.4) == -5.8)
  # Building 5
  r = SymmetricPitchedRoof(name="", alpha=32, H_First=11.0, H_Dach=4.9, b=18.6, l=15.6, h=0)
  assert(r.H_A2(beta=76, l_A=16.5, H_First=10.4, H_U=0.4) == 0.3)

def test_fromdict():
  d = {'fid': 8,
  'hoehe': 223.6,
  'id': 'G1',
  'alpha': 0,
  'l': 10.7,
  'b': 7.5,
  'schornstein': True,
  'typ': 'Flachdach',
  'a': 0,
  'h_dach': 0,
  'h_first': 6.5,
  'l_a': 0.0,
  'beta': 0.0 }

  fr = Roof.from_dict(d)
  assert(type(fr) == FlatRoof)

  d['typ'] = 'Satteldach'
  sr = Roof.from_dict(d)
  assert(type(sr) == SymmetricPitchedRoof)