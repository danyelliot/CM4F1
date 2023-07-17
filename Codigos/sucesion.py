import numpy as np
def succession(n):
  if n==0:
    u=0.00805345
  else:
    aux1=succession(n-1)
    u=(1/n)-5*aux1
  return u



for n in range(0,21):
  u=succession(n)
  print("El termino ",20-n," de la sucesión en python es:",u)

