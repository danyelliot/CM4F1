import numpy as np
np.set_printoptions(precision=8,suppress=True)
def QRschmith(A):
    m,n= np.shape(A)
    Q=np.zeros((m,n),float)
    R=np.zeros((n,n),float)
    w=np.zeros((m,1),float)
    for k in range(0,n):
        w=A[:,k]
        for j in range(0,k):
            R[j][k]=np.dot(np.transpose(Q[:,j]),w)
        for j in range(0,k):
            w=w-R[j][k]*Q[:,j]
        R[k][k]=np.linalg.norm(w)
        Q[:,k]=(1/R[k][k])*w
    return Q,R

def QRschmithModificado(A):
    m,n= np.shape(A)
    Q=np.zeros((m,n),float)
    R=np.zeros((n,n),float)
    w=np.zeros((m,1),float)
    for k in range(0,n):
        w=A[:,k]
        for j in range(0,k):
            R[j][k]=np.dot(np.transpose(Q[:,j]),w)
            w=w-R[j][k]*Q[:,j]
        R[k][k]=np.linalg.norm(w)
        Q[:,k]=(1/R[k][k])*w
    return Q,R

A=np.array([
    [1,2,4],
    [4,2,1],
    [2,3,4]],float)

Q,R=QRschmithModificado(A)
print('\nMetodo de Gram-Schmidt:')
print('La matriz Q: ')
print(Q)
print('\nLa matriz R: ')
print(R)
b=np.array([35,34,42],float)
solucion = np.dot(np.dot(np.linalg.inv(R),np.transpose(Q)),b)
print("\nSolucion: ",np.round(solucion,decimals=5),"\n")
