import numpy as np
A = np.array([[15,12,25],
            [10,20,20],
            [20,30,30]],float)
NIA=np.linalg.norm(A, np.inf)
print("La norma infinita de la matriz es: ",NIA)
inversa=np.linalg.inv(A)
print("La matriz inversa es: ")
print(inversa)
NIIA=np.linalg.norm(inversa, np.inf)
print("La norma infinita de la inversa de la matriz es: ",NIIA)
print('Por lo tanto el número de condicionamiento de la matriz es: ',
    NIA*NIIA)