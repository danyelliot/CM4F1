import numpy as np

def LDLT(a):
    m, n = a.shape
    if (m !=n ):
        print("LDLT cannot be used.") #Ensure that the number of equations is equal to the number of unknowns
    else:
        l = np.zeros((n,n))
        d = np.zeros((n,n))
        s1 = 0
        s2=0
        for j in range(n):
            l[j][j] = 1
            for r in range(j): s1+=((l[j][r])**2)*(d[r][r])
            d[j][j]=a[j][j]-s1
            s1=0
            if(d[j][j]==0): continue               
            for i in range(j+1, n):
                for r in range(j): s2+=l[i][r]*l[j][r]*d[r][r]
                l[i][j] = (a[i][j] - s2) / d[j][j]
                s2 = 0                #Initialize s2 after each summation=0
        print("La matriz diagonal es:")
        print(d)
        print("La matriz triangular inferior es:")
        print(l)
        print("La matriz triangular superior es:")
        u=np.dot(d,np.transpose(l))
        print(u)
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

a = np.array([[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]],float)
b = np.array([9,23,22,47])
print("Respuesta:")
LDLT(a)