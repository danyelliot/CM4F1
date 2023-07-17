import numpy as np

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
    Jf=np.zeros((3,3))
    Jf[:,0]=np.transpose([2*x[0]-1,2*x[1],2*x[2]])
    Jf[:,1]=np.transpose([2*x[0],2*x[1]-1,2*x[2]])
    Jf[:,2]=np.transpose([2*x[0],2*x[1],2*x[2]+1])
    L=np.linalg.norm(Jf,np.inf)
    if L<1:
        return True 
    return False

def f(x):
    
    ft=np.zeros((3,1))
    ft[0,0]=(x[0]**2-x[0]+x[1]**2+x[2]**2-5)
    ft[1,0]=(x[0]**2+x[1]**2-x[1]+x[2]**2-4)
    ft[2,0]=(x[0]**2+x[1]**2+x[2]**2+x[2]-6)
    return ft 

x0=np.array([0,0,0])
PuntoFijoSist(J,f,x0,tol=1E-7)