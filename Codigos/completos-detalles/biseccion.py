from numpy import log as ln
import numpy as np
from tabulate import tabulate

def biseccion(f, a, b, tol=1.0e-6):
    if a > b:
        raise ValueError("Intervalo mal definido")
    if f(a) * f(b) >= 0:
        raise ValueError("La función debe cambiar de signo en el intervalo")
    if tol <= 0:
        raise ValueError("La cota de error debe ser un número positivo")

    i = 0
    results = []
    c1=0
    while abs(a - b) >= tol:
        i += 1
        c = (a + b) / 2
        fa = f(a)
        fb = f(b)
        error = abs(c-c1)
        fc = f(c)
        if f(c) == 0:
            a = b = 0
        elif fb * f(c) >= 0:
            b = c
        else:
            a = c
        results.append([i-1, a, b, c, fa, fb, fc, error])
        c1=c


    print(tabulate(results, headers=["Iteración", "a", "b", "c", "f(a)", "f(b)", "f(c)", "Error"], tablefmt="grid"))
    print('El número de iteraciones es:', i-1)
    return c

f = lambda x: x**(2) -7

# Método de Bisección
sol = biseccion(f, 2, 3, 1.0e-5)
print("Solución aproximada por Bisección:", sol)
monto = 5.0
print("Vuelto a 2 decimales:",monto,"-",sol,"=",np.round(5-sol,2))