import numpy as np
def DoolittleL1(a):
    m, n = a.shape
    if (m !=n ):
        print("Doolittle cannot be used.")#Ensure that the number of equations is equal to the number of unknowns
    else:
        l = np.zeros((n,n))
        u = np.zeros((n,n))
        s1 = 0
        s2 = 0
        for i in range(n):
            l[i][i] = 1
        for k in range(n):
            for i in range(k+1):
                for r in range(i): s1 += l[i][r] * u[r][k]
                u[i][k] = a[i][k] - s1
                s1 = 0                #Initialize s1 after each summation=0
            for i in range(k, n):
                for r in range(k): s2 += l[i][r] * u[r][k]
                l[i][k] = (a[i][k] - s2) / u[k][k]
                s2 = 0                #Initialize s2 after each summation=0
        print('La matriz U es:')
        print(u)
        print('La matriz L es:')
        print(l)
        solution(u,l)

def solution(u,l):
    m, n = a.shape  
    y = np.zeros(n)
    s3 = 0
    y[0] = b[0]/l[0][0]   # First calculate the first x solution
    for k in range(1, n):
        for r in range(k):
            s3 += l[k][r] * y[r]
        y[k] = (b[k]-s3) / l[k][k]
        s3 = 0            #Back generation to solve
    x = np.zeros(n)
    s4 = 0
    x[n-1] = y[n-1]/u[n-1][n-1]
    for k in range(n-2, -1, -1):
        for r in range(k+1, n):
            s4 += u[k][r] * x[r]
        x[k] = (y[k] - s4)/u[k][k]
        s4 = 0
    for i in range(n):
        print("x" + str(i + 1) + " = ", x[i])
    print("x" " = ", x)

a = np.array([[2,2,1],[4,7,2],[2,11,5]])
b = np.array([9,23,22])
print("Respuesta:")
DoolittleL1(a)
