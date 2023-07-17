import numpy as np

# Set print options (optional)
np.set_printoptions(precision=8, suppress=True)

def determinante(R):
    det=1
    for i in range(len(R)):
        det*=R[i,i]
    return det

def Householder(A):
    R=A
    n,m=np.shape(A)
    Q=np.identity(n)
    aux=0
    if n>=m:
        aux=m
    else:
        aux=n
    for k in range(aux):
        a=np.array(A[:,0])
        e1=np.zeros((1,n-k))
        e1[0,0]=1
        v=a+np.sign(A[0,0])*np.linalg.norm(a)*e1
        aux2=np.dot(v,v.T)
        H=np.identity(n-k)-(2/aux2[0,0])*np.dot(v.T,v)
        aux3=np.dot(H,A)
        A=np.array(aux3[1:,1:])
        H_modificado=transformarH(H,n,k)
        Q=np.dot(Q,H_modificado)
        R=np.dot(H_modificado,R)
    return Q,R


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

A=np.array([
    [2, 1,1],
    [1, 2,1],
    [1 ,1,1 ]],float)
b=np.array([2,4,6,8,13],float)
b=np.transpose(b)

Q,R=Householder(A)
print('La matriz Q es:')
print(Q)
print('La matriz R es:')
print(R)

""" print('El determinante de la matriz es: ')
det = determinante(R)
print(det)

solucion = np.dot(np.dot(np.linalg.inv(R),np.transpose(Q)),b)
solucion=np.transpose(solucion)
print("solucion: ",np.round(solucion,decimals=5)) """