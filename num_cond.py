import numpy as np

def num_cond(A):
  print('La matriz A es: ')
  print(A)
  print('La matriz inversa de A es: ')
  invA=np.linalg.inv(A)
  print(invA)
  print('La norma infinita de A es:',end=" ")
  inf_A=np.linalg.norm(A, np.inf)
  print(inf_A)
  print('La norma infinita de la inversa A es:',end=" ")
  inf_invA=np.linalg.norm((invA), np.inf)
  print(inf_invA)
  print('Entonces: ')
  cond=inf_A*inf_invA
  print('El numero de condicionamiento de la matriz A es: ',cond)

A = np.array([[2/9,1/4,2/9],[1/3,1/3,5/18],[4/9,5/12,1/2]],float)
num_cond(A)


