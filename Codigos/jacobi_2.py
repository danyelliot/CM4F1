import numpy as np

# |x(k+1) - x(k)| < tol
# Entrada:  A, b, x0, tol
# Salida: x, k

def Jacobi(A,b,x0,tol,maxiter):
    n = len(A)
    x = np.zeros(n)
    k = 0
    xant = np.copy(x0)

    print("J = I-D^-1*A")
    print("D = diag(A)")
    print("c = D^-1*b")
    print("x(k+1) = J*x(k) + D^-1*b")
    print("x(k+1) = J*x(k) + c")
    while k < maxiter:
        k = k + 1
        
        for i in range(n):
            x[i] = (b[i] - np.dot(A[i,:],x) + A[i,i]*x[i]) / A[i,i]
        print('x_',k,'=', x)
        if max(abs(x-xant)) < tol:
            print('converge')
            break
        xant = np.copy(x)

    return x, k

# main 

A = np.array([[9,8,9],[5,10,4],[2,4,8]],dtype='double')
b = np.array([170,117,98])

x0 = np.array([4,4,5])
tol = 1e-4
maxiter = 100

x, k = Jacobi(A,b,x0,tol,maxiter)
print ('x = ', x)
print ('k = ', k)
