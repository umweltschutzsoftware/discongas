from math import pi, sin


import math

def upstreamsinglebuilding(l_V, b_V, beta, H_First):
  l_eff = l_V * math.sin(beta * math.pi / 180) + b_V * math.cos(beta * math.pi / 180)
  l_rz = (1.75*l_eff)/(1+0.25*l_eff/H_First)
  return round(l_rz,1)