import numpy as np

def determinante(R):
    det=1
    for i in range(len(R)):
        det*=R[i,i]
    return det

def Householder(A):
    R=A
    n=len(A)
    Q=np.identity(n)
    T=A
    for k in range(n):
        a=np.matrix(A[:,0])
        e1=np.zeros_like(a)
        e1[0,0]=1
        v=a+np.sign(A[0,0])*np.linalg.norm(a)*e1
        aux2=np.dot(v.T,v)
        H=np.identity(n-k)-(2/aux2[0,0])*np.dot(v,v.T)
        aux=np.dot(H,A)
        A=np.matrix(aux[1:,1:])
        H_modificado=transformarH(H,n,k)
        print("------------------------------------------")
        print('H',k+1,':\n' )
        print(H_modificado)
        if k <= n-2:
            T=np.dot(H_modificado,T)
            T=np.dot(T,np.transpose(H_modificado))
        Q=np.dot(Q,H_modificado)
        R=np.dot(H_modificado,R)
    Q=np.round(Q, decimals=9)
    R=np.round(R, decimals=9)
    T=np.round(T,decimals=9)
    return Q,R,T


def transformarH(H,n,k):
    H_modificado=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if i<k or j<k:
                if i==j:
                    H_modificado[i][i]=1
                else:
                    H_modificado[i][j]=0
            else:
                H_modificado[i,j]=H[i-k,j-k]
    return H_modificado



A=np.matrix([
    [1,1,1],
    [12,10,9],
    [2,-1,0]
    ],float)
b=np.matrix([44,436,0],float)
b=np.transpose(b)

Q,R,T=Householder(A)
Q=-Q
R=-R
print("------------------------------------------")
print('Q = (H1)(H2)\n')
print(Q)
print("------------------------------------------")
print('R = (H2)(H1)(A)\n')
print(R)
print("------------------------------------------")
print('T =')
print(T)
print("------------------------------------------")

det = determinante(R)
print('det :',det)

print("------------------------------------------")
print("c = (Q^T)(b)\n")

print(np.dot(np.transpose(Q),b))
print("------------------------------------------")

solucion = np.dot(np.dot(np.linalg.inv(R),np.transpose(Q)),b)
solucion=np.transpose(solucion)
print("Solución x = (R^-1)(Q^T)(b) \n")
print(np.round(solucion,decimals=5))