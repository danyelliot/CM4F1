import math
import numpy as np
from numpy.core.fromnumeric import transpose

def gradienteConjugado(A,B,tol):
    x = np.transpose([-5.05, 80.05, 0])
    r=B
    d=(np.linalg.norm(r))**2
    k=1
    try:
        while math.sqrt(d)>tol*np.linalg.norm(B) and k<=100:
            if k == 1: 
                p=r
            else:
                b=d/auxD2
                p=r+b*p
            w=np.dot(A,p)
            a=d/(np.dot(np.transpose(p),w))
            x=x+a*p
            r=r-a*w
            auxD2=d
            d=(np.linalg.norm(r))**2
            print("La matriz X",(k)," es:")
            print(x)
            #print (x[:,1])
            k+=1
    except:
        print('El metodo no converge')

def matrizHilbert(n):
    A=np.zeros((n, n))
    B=np.zeros((n,1))
    for i in range(0,n):
        aux=0
        for j in range(0,n):
            A[i,j]=1/(3+i+j)
            aux+=A[i,j]
            B[i,0]=(1/3)*aux
    return A,B

def matriz(n):
    A=np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if j==i:
                A[i,j]=2*i
            elif j==i+1 or j==i-1 :
                [i,j]=-1
    return A

def matriz2(n):
    A=np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if j==i:
                A[i,j]=4
            elif (j==i+1 and i%5!=4) or (j==i-1 and j%5!=4) or j==i+5 or j==i-5 :
                A[i,j]=-1
    return A

tol =1.0e-5
A = np.array([[0, 0, 1],
            [64, 8, 1],
            [256, 16, 1]],float)

b= np.transpose([0, 320, 0])
gradienteConjugado(A,b,tol)







#tol = np.finfo(float).eps
""" tol =1.0e-5
A=matriz(40)
b=np.array([1.5*i-6 for i in range(1,41)])
b=np.transpose(b)
gradienteConjugado(A,b,tol) """



""" tol =1.0e-5
A=matriz2(25)
b=np.array([1, 0, -1, 0, 2, 1, 0, -1, 0, 2, 1, 0, -1, 0, 2, 1, 0, -1, 0, 2, 1, 0, -1, 0, 2])
b=np.transpose(b)
gradienteConjugado(A,b,tol)
 """

""" b = np.array([1.902207, 1.051143, 1.175689, 3.480083, 0.819600, -0.264419, -0.412789, 1.175689, 0.913337
, -0.150209, -0.264419, 1.051143, 1.966694, 0.913337, 0.819600, 1.902207])
b=np.transpose(b)
A=matriz2(16)
gradienteConjugado(A,b,tol)
"""


""" for i in range(2,10):
        print("Para la matriz de hilbert de orden "+str(i)+" el desarrollo es: ")
        A=matrizHilbert(i)
        gradienteConjugado(A,B,tol)  """