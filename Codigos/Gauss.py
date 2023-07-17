import numpy as np
import sys

def GJ(a):
    n=len(a)
    
    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('No se puede dividir entre cero...')
        for j in range(n):
            if i != j:
                ratio = a[j][i] / a[i][i]
                for k in range(n + 1):
                    a[j][k] = a[j][k] - ratio * a[i][k]

    return a

A = np.array([[2., 1., 0.,4.],
            [-4., -2.0, 3.0,-7.0],
            [4., 1.0,-2 , 8],
           [0 ,-3, -12, -1]])
B = np.array([[2],
              [-9],
              [2],
              [2]])
AB = np.concatenate((A, B), axis=1)
print(GJ(AB))