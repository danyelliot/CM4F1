import numpy as np

fx  = lambda x: x**4+5*x**3+77*x**2+153*x+90
dfx = lambda x: 4*x**3+15*x**2+154*x+153

x0 = -1+1j
tolera = 0.0000001

tabla = []
tramo = abs(2*tolera)
xi = x0
while (tramo>=tolera):
    xnuevo = xi - fx(xi)/dfx(xi)
    tramo  = abs(xnuevo-xi)
    tabla.append([xi,xnuevo,tramo])
    xi = xnuevo


tabla = np.array(tabla)
n = len(tabla)

print("Calle Cuadros Sergei-20184099J")
print("pregunta 3:")
print(['xi', 'xnuevo', 'tramo'])
np.set_printoptions(precision = 4)
print(tabla)
print('raiz en: ', xi)
