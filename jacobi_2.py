import numpy as np

# |x(k+1) - x(k)| < tol
# Entrada:  A, b, x0, tol
# Salida: x, k

def Jacobi(A,b,x0,tol,maxiter):
    n = len(A)
    x = np.zeros(n)
    k = 0
    xant = np.copy(x0)
    while k < maxiter:
        k = k + 1
        for i in range(n):
            x[i] = (b[i] - np.dot(A[i,:],x) + A[i,i]*x[i]) / A[i,i]
        if max(abs(x-xant)) < tol:
            print('converge')
            break
        xant = np.copy(x)
    return x, k

# main 

A = np.array([[0.3, -0.3 , 0.2],[-0.3, 0.1, 0.1],[1, 0, -1]],dtype='double')
b = np.array([0,0,-100])

x0 = np.zeros(3)
tol = 1
maxiter = 100

x, k = Jacobi(A,b,x0,tol,maxiter)
print ('x = ', x)
print ('k = ', k)

x = np.linalg.solve(A,b);
print ('x = ', x)
