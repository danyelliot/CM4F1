import numpy as np
import matplotlib.pyplot as plt


def CirculoGershgorin(A):
    m,n=np.shape(A)
    if m!=n:
        print('La matriz debe ser cuadrada')
        return
    figure, axes = plt.subplots()
    rangofinal=[]
    for i in range(n):
        di=0
        sum=0
        for j in range(m):
            if i==j:
                di=A[i,j]
            else:
                sum+=abs(A[i,j])
        rango=[di-sum,di+sum]
        rangofinal.extend(rango)
        print('El intervalo para la fila '+str(i+1)+' es: '+ str(rango))
        circle = plt.Circle((di.real, di.imag ), sum ,fill = False )
        axes.add_artist( circle )
    rangoespectral=[]
    maxi=max(np.abs(rangofinal))
    if maxi in rangofinal:
        idx=rangofinal.index(maxi)
        aux=rangofinal[idx-1:idx+1]
        rangoespectral.extend(aux)
    else:
        idx=rangofinal.index(-maxi)
        aux=[rangofinal[idx+1],abs(rangofinal[idx])]
        rangoespectral.extend(aux)
    print('El radio espectral pertenece al intervalo: ',str(rangoespectral))
    autovalores,autovectores=np.linalg.eig(A)
    print('Los autovalores son: ')
    print(autovalores)
    x=autovalores.real
    y=autovalores.imag
    radioespectral=max(np.abs(autovalores))
    print('Por lo tanto el radio espectral es: ',radioespectral)
    axes.set_aspect(1) 
    plt.title( 'Gersgorin Circle' ) 
    plt.xlim( -maxi-1 , maxi+1 ) 
    plt.ylim( -maxi-1 , maxi+1 ) 
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    plt.plot(x,y,'o', label = 'Puntos')
    plt.show() 


A=np.array([[-1+1j, 0, 1/4],
            [1/4, 1, 1/4],
            [1, 1, 3]])
CirculoGershgorin(A)
