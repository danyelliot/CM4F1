import numpy as np

def traza(A,n):
    tr = 0
    for i in range(n):
        tr += A[i][i]
    return tr

def Leverrier(A,n):
    a = np.zeros(n)
    s = np.zeros(n)
    t_A = A
    for i in range(n):
        s[i] = traza(t_A,n)
        t_A = np.dot(t_A,A)

    for i in range(n):
        sum = s[i]
        if(i>0):
            k = 0
            for j in range(i-1,-1,-1):
                sum += s[j]*a[k]
                k += 1
        a[i] = -sum/(i+1)
    return a

M = np.array([[0.5, 0.3, 0.5],
                [0.25, 0.4, 0.25],
                [0.25, 0.3, 0.25]],float)
print(Leverrier(M,3))