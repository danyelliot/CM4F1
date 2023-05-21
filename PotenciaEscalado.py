import numpy as np

np.set_printoptions(suppress=True)

def PotenciaEscalada(A,x,tol):
    k=0
    aux=np.array([[0,0,0]]).T
    aux2=np.amax(x)
    print('k=',k,'  x_',k,'=',x.T)
    while np.linalg.norm(x-aux,np.inf)>=tol:
        aux=x
        k=k+1
        x=np.dot(A,x)
        aux2=np.amax(abs(x))
        x=x/aux2
        print('k=',k,'  x_',k,'=',x.T,' r_',k,'=',aux2)
    print("El autovalor dominante es ",aux2)
    print("El numero de iteraciones es ",k)
    return np.transpose(x)

x = np.array([[1,1,0]]).T
A = np.array([[2, 0, 2],
            [-1, 2, 1],
            [0, 1, 4]])
x=PotenciaEscalada(A,x,1.0e-12)
print(x)