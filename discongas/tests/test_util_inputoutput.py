from discongas.util.inputoutput import additiveterm


from discongas.util.inputoutput import *

def test_additiveterm():
  assert(additiveterm(400, 2) == 0.4)
  assert(additiveterm(380, 0.5) == 0.4)
  assert(additiveterm(400, 0.5) == 0.4)
  assert(additiveterm(420, 0.5) == 1.0)
  assert(additiveterm(420, 3) == 3.0)