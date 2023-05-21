import numpy as np



def TransformadaFourier(m,f):
    N=2**m
    w=np.exp(-1j*2*np.pi/N)
    Z=list()
    C=list()
    D=list()
    for k in range(N):
        Z[k]=w**k
        C[k]=f(2*np.pi*k/N)
    for n in range(m):
        for k in range(2**(m-n-1)):
            for j in range(2**n):
                u = C[(2**n)*k + j]
                v = Z[j*2**(m - n - 1)]*C[(2**n)*k + j+(2**m-1)]
                D[(2**(n+1))*k + j] = (u+v)/2
                D[(2**(n+1))*k + j+(2**n)] = (u-v)/2
        for j in range(N):
            C[j]=D[j]
    return C







