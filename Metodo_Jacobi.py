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
            print('\nEl método converge\n')
            break
        xant = np.copy(x)
    return x, k

# main 

A = np.array([[4,-1,0,-1,0,0],[-1,4,-1,0,-1,0],[0,-1,4,0,0,-1],[-1,0,0,4,-1,0],[0,-1,0,-1,4,-1],[0,0,-1,0,-1,4]],dtype='double')
b = np.array([56,25,62,41,10,47])

x0 = np.zeros(6)
tol = 1e-5
maxiter = 100

x, k = Jacobi(A,b,x0,tol,maxiter)
print ('x = ', x)
print ('k = ', k)

x = np.linalg.solve(A,b);
print ('x = ', x)
