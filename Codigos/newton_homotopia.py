import numpy as np
def newton_homotopia(F,J,x0,Tol):
    x , error , n  = x0 , 1E3 , 0
    print(f'iteracion\t\tdx\t\t\t\tx\t\t\t\terror\n')
    print(f'{n}\t\t-\t\t\t\t{x}\t\t\t\t-')
    while error > Tol:
        dx = -np.linalg.solve(J(*x),F(*x))
        x , error = x + dx , np.linalg.norm(dx)
        n += 1
        print(f'{n}\t\t{dx}\t\t{x}\t\t{error}')
    return x

F = lambda x,y: [x-2*y**2,3*x-y-5]
dF = lambda x,y: [[1,-4*y],[3,-1]]

x0 = np.array([5,4])
Tol = 1E-4
print('solucion: ',newton_homotopia(F,dF,x0,Tol))
