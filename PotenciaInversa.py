import numpy as np

def PotenciaInversa(A,x,o,tol):
    k=0
    aux2=0
    while True:
        k+=1
        aux=x
        x=np.dot(np.linalg.inv(A),x)
        aux2=np.amax(abs(x))
        if aux2  not in x:
            aux2=-aux2
        x=x/aux2
        aux2=o+1/aux2
        print('k=',k,'  x_',k,'=',x.T,' r_',k,'=',aux2)
        if np.linalg.norm(x-aux)<tol:
            break
    print("El autovalor dominante es {}".format(aux2))
    print("El numero de iteraciones es {}".format(k))
    return np.transpose(x)

A = np.array([[-4, 14, 0],
                [-5, 13, 0],
                [-1, 0 ,2]],float)

x=np.transpose(np.matrix([1.0,1.0,1.0]))
o=(float)(np.dot(x.T,np.dot(A,x))/(np.dot(x.T,x)))
A=A-o*np.identity(3)

x=PotenciaInversa(A,x,o,1.0e-5)
print(x)