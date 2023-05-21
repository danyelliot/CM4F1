import numpy as np
from numpy import pi as PI

def fft1(f,N):  
    w = np.exp(-2*PI*1j/N) # 1j es la variable compleja    
    C =  np.zeros( (N,),dtype=complex)
    xx = np.linspace(0,2*PI*(N-1.0)/N,N)    
    C[:]= f(xx)    
    D = np.zeros_like(C)
    Z = np.array([w**k for k in range(N)])
    for n in range(m):
        for k in range(2**(m-n-1)):
            for j in range(2**(n)):
                u = C[2**n * k + j]
                v = Z[j*2**(m-n-1)]*C[2**n * k + 2**(m-1) + j]
                D[2**(n+1) * k + j] = (u+v)/2
                D[2**(n+1) * k + j + 2**n] = (u-v)/2            
        C[:]=D[:]
    return C

g = lambda x : x**4-3*x**3+2*x**2-np.tan(x*(x-2))
a = 0
b = 2 
z = lambda x : a+x*(b-a)/(2*PI)
f = lambda x : g(z(x))
m=3
N=2**m                  
C = fft1(f,N)
print("C=",C) 
A = 2*C[0:N//2].real
A[0]  = 0.5*A[0]
B = -2*C[0:N//2].imag
print("A=",A);print("B=",B)
import matplotlib.pyplot as plt
xx = np.linspace(0,2*PI,100) 
yy = sum([ (A[k]*np.cos(k*xx)+B[k]*np.sin(k*xx))[:,None] for k in range(len(A))])
tt = np.linspace(0,2*PI*(N-1.0)/N,N) 
plt.plot(z(xx),yy,z(tt),f(tt),'*')  
plt.show()
