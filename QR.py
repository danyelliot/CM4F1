import numpy as np
import scipy
from scipy import linalg

#Se define los valores de la matriz A

A=np.array([
    [1,2,4],
    [4,2,1],
    [2,3,4]],float)
q,r=scipy.linalg.qr(A)
b=np.array([35,34,42],float)
b=np.transpose(b)
y = np.dot(q.T,b)
xqr = scipy.linalg.solve(r,y) 


print('\nA:\n', A) 
print('\nQ:\n', q*-1) 
print('\nR:\n', r*-1) 
print ("Solucion: ")
print (xqr.T,"Rx=y")