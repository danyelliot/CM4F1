import math
import numpy as np

def RDescensoRapido(A,B):
    eps = 1E-5
    x = np.array(np.transpose([-5.05, 80.05, 0]))
    r=B
    i=0
    while np.linalg.norm(r)>=eps*np.linalg.norm(B):
        t=np.dot(np.transpose(r),r)/np.dot(np.transpose(r),np.dot(A,r))
        x=x+t*r
        r=B-np.dot(A,x)
        print("La matriz X en la iteracion ",(i+1)," es:")
        i=i+1
        print(x)
        if i==100:
            print('El metodo no converge')
            return

A = np.array([[0,0,1],[64,8,1],[256,16,1]],float)

b= np.transpose(np.array([0, 320, 0]))
RDescensoRapido(A,b)
print(np.linalg.solve(A,b))
