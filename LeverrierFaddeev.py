import numpy as np

def Leverrier_Faddeev(A):
    m, n = A.shape 
    I = np.eye(n)
    B = np.zeros((n+1,n,n))
    c = np.zeros(n+1)
    
    c[0] = 1.0
    B[0] = I
    
    for k in range(1,n):
        c[k] = - 1/k * np.trace(np.dot(A,B[k-1]))
        B[k] = np.dot(A,B[k-1]) + c[k]*I
        
    c[n] = - 1/n * np.trace(np.dot(A,B[n-1]))
    determinante = (-1)**n * c[n]
    
    if c[0]!=0:
        inversa = -1/c[n] * B[n-1]
    else:
        inversa = np.zeros((n,n)) * np.nan
    print('p(x) =', c)
    print('determinante =', determinante)
    print('inversa =')
    print(inversa)

A = np.array([[0.5, 0.3, 0.5],
                [0.25, 0.4, 0.25],
                [0.25, 0.3, 0.25]],float)
Leverrier_Faddeev(A)

