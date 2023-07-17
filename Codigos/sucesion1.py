def succession(n):
  if n==0:
    u=ini
  else:
    aux1=succession(n-1)
    u=3.9*aux1*(1-aux1)
  return u



for n in range(0,21):
  u=succession(n)
  print("El termino ",n," de la sucesión en python es:",u)

for n in range(0,21):
  u=succession(n,0.501)
  print("El termino ",n," de la sucesión en python es:",u)

for n in range(0,21):
  u=succession(n,ini=0.51)
  print("El termino ",n," de la sucesión en python es:",u)