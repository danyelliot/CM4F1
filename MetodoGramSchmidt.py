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
    [300,0,150],
    [0,1000,-150],
    [1,-1,-1]],float)

Q,R=QRschmithModificado(A)
print('Metodo de Gram-Schmidt:')
print('La matriz Q: ')
print(Q)
print('La matriz R: ')
print(R)
b=np.array([7.5,11.5,0],float)
solucion = np.dot(np.dot(np.linalg.inv(R),np.transpose(Q)),b)
print("solucion: ",np.round(solucion,decimals=5))
