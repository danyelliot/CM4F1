import numpy as np
from math import cos,sin,sqrt
def PuntoFijoSist(J,f,x,tol=1.0e-6):
    k=0
    print("La solucion para la iteracion numero",k,"es: ");
    print(x)
    while J(x) and abs((f(x)-x>tol).any()):
        x=f(x)
        k+=1
        print("La solucion para la iteracion numero",k,"es: ");
        print(x)
    if not J(x):
        print('El metodo no converge')
    else:
        print("El metodo termino con "+str(k)+" iteraciones")
        print('La respuesta es: ')
        print(np.round(x,6))

def J(x):
    Jf=np.zeros((2,2))
    Jf[:,0]=np.transpose([x[0]/5,(x[1]**2+1)/10])
    Jf[:,1]=np.transpose([x[1]/5,(x[1]**2)*(x[0])/5])
    L=np.linalg.norm(Jf,np.inf)
    if L<1:
        return True 
    return False

def f(x):
    ft=np.zeros((2, 1))
    ft[0,0]=(x[0]**2+x[1]**2+8)/10
    ft[1,0]=(x[0]*x[1]**2+x[0]+8)/10
    return ft 

x0=np.array([0,0])
PuntoFijoSist(J,f,x0,tol=1E-7)