import numpy as np

def Crout(a): 
    m, n = a.shape
    if (m !=n ):
        print("CroutU1 cannot be used.")
    else:
        l = np.zeros((n,n))
        u = np.zeros((n,n))
        s1 = 0
        s2 = 0
        for i in range(n):
            u[i][i] = 1
        for k in range(0, n):
            for i in range(k, n):
                for r in range(k): s1 += l[i][r] * u[r][k]
                l[i][k] = a[i][k] - s1
                s1 = 0                
            for j in range(k+1, n):
                for r in range(k): s2 += l[k][r] * u[r][j]
                u[k][j] = (a[k][j] - s2) / l[k][k]
                s2 = 0               
        mostrar(u,l)

def Doolittle(a):
    m, n = a.shape
    if (m !=n ):
        print("Doolittle cannot be used.")
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
                s1 = 0                
            for i in range(k, n):
                for r in range(k): s2 += l[i][r] * u[r][k]
                l[i][k] = (a[i][k] - s2) / u[k][k]
                s2 = 0               
        mostrar(u,l)

def mostrar(u,l):
    print('La matriz U es:')
    print(u)
    print('La matriz L es:')
    print(l)
    solution(u,l)

def solution(u,l):
    m, n = a.shape  
    y = np.zeros(n)
    s3 = 0
    y[0] = b[0]/l[0][0]   
    for k in range(1, n):
        for r in range(k):
            s3 += l[k][r] * y[r]
        y[k] = (b[k]-s3) / l[k][k]
        s3 = 0            
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

def pedido(a):
    print("Con Crout:")
    Crout(a)
    print("Con Doolittle:")
    Doolittle(a)
    print("\n\n")

a = np.array([[4,1,2],[3,1,4],[5,1,3]])
b = np.array([19,25,25])
b = np.transpose(b)

print("Pedido 1:")
pedido(a)
b = np.array([13,16,16])
b = np.transpose(b)
print("Pedido 2:")
pedido(a)
b = np.array([8,12,10])
b = np.transpose(b)
print("Pedido 3:")
pedido(a)