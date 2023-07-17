import numpy as np

def Jacobi(a,x):
    TOL = 1E-3 ; maxiter = 100
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

n = 3
a = np.array([0.3, -0.3 , 0.2,-0.3, 0.1, 0.1, 1, 0, -1],dtype='f4')
a = np.reshape(a,(n,n))
b = np.array([0,0,-100],dtype='f4')
x = np.zeros(n,dtype='f4')

x,cambio_rel,cont = Jacobi(a,x)

# Solucion exacta
x_exacta = np.linalg.solve(a,b)
print("Solucion exacta: ",x_exacta)
