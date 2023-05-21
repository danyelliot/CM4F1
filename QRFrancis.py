import numpy as np

np.set_printoptions(suppress=True)

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
    Q=np.round(Q, decimals=9) 
    R=np.round(R, decimals=9) 
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

def es_matriz_diagonal(m):
    n=len(m)
    for i in range(n): 
        for j in range(n): 
            if ((i != j) and (m[i,j] != 0 or m[i,j]!=-0)): 
                return False  
    return True

def QRFrancis(A):
    i=0
    while not es_matriz_diagonal(A):
        print('Matriz A en la iteracion '+str(i)+' es:')
        print(A)
        Q,R=Householder(A)
        A=np.dot(R,Q)
        A=np.round(A,decimals=5)
        i+=1
    print('Matriz A en la iteracion '+str(i)+' es:')
    print(A)
    autovalores=np.diag(A)
    return autovalores


A=np.array([[1, 2, 3],[2 ,2, 3],[3, 3, 3]])
autovalores=QRFrancis(A)
print('Los autovalores son: ',autovalores)
