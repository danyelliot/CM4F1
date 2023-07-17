import numpy as np

def Jacobi(a,x):
    TOL = 1E-6 ; maxiter = 100
    cambio_rel = 1
    cont = 0
    y = np.zeros_like(x)
    while cambio_rel > TOL and cont < maxiter:
        print("x=["+(" "*5).join(list(map('{:5.3f}'.format,x)))+"]")
        for i in range(n):
            idx = [j for j in range(n) if j != i]
            y[i] = (b[i] - np.dot(a[i,idx],x[idx])) / a[i,i]
        cambio_rel = np.linalg.norm(x-y,np.inf)/np.linalg.norm(y,np.inf)
        x = np.copy(y)
        cont += 1
        print("x=["+(" "*5).join(list(map('{:5.3f}'.format,x)))+"]")
        if cambio_rel <= TOL:
            print("Converge ")
        else:
            print("No converge")
        print(f"Metodo terminado en {cont} iteraciones. ||x-y||/||y|| = {cambio_rel}")
        return (x,cambio_rel,cont)

n = 6
a = np.array([[4,-1,0,-1,0,0,-1,4,-1,0,-1,0,0,-1,4,0,0,-1,-1,0,0,4,-1,0,0,-1,0,-1,4,-1,0,0,-1,0,-1,4]],dtype='f4')
a = np.reshape(a,(n,n))
b = np.array([56,25,62,41,10,47],dtype='f4')
x = np.zeros(n,dtype='f4')

x,cambio_rel,cont = Jacobi(a,x)

