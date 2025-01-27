import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
from tabulate import tabulate
np.set_printoptions(precision=5, suppress=True)


def diferenciasDividas(xi, fi):
    titulo = ['i', 'xi', 'fi']
    n = len(xi)
    ki = np.arange(n)
    tabla = np.concatenate(([ki], [xi], [fi]), axis=0)
    tabla = np.transpose(tabla)
    dfinita = np.zeros(shape=(n, n - 1), dtype=float)
    tabla = np.concatenate((tabla, dfinita), axis=1)
    [n, m] = np.shape(tabla)
    diagonal = n - 1
    j = 3

    while j < m:
        titulo.append('F[' + str(j - 2) + ']')
        i = 0
        paso = j - 2
        while i < diagonal:
            denominador = (xi[i + paso] - xi[i])
            numerador = tabla[i + 1, j - 1] - tabla[i, j - 1]
            tabla[i, j] = numerador / denominador
            i = i + 1
        diagonal = diagonal - 1
        j = j + 1

    dDividida = tabla[0, 3:]
    n = len(dfinita)
    x = sym.Symbol('x')
    polinomio = fi[0] + dDividida[0] * (x - xi[0]) + dDividida[1] * (x - xi[0]) * (x - xi[1])

    polisimple = polinomio.expand()
    px = sym.lambdify(x, polisimple)

    muestras = 101
    a = np.min(xi) - 3
    b = np.max(xi) + 3
    pxi = np.linspace(a, b, muestras)
    pfi = px(pxi)

    tabla_str = tabulate(tabla, headers=titulo, floatfmt=".5f", tablefmt="fancy_grid")
    print('Tabla Diferencia Dividida')
    print(tabla_str)
    print('dDividida:')
    print(dDividida)
    print('polinomio:')
    print(polinomio)
    print('polinomio simplificado:')
    print(polisimple)

    error = np.abs(fi - px(xi))
    print('Error:')
    print(error)

    plt.plot(xi, fi, 'o', label='Puntos')
    plt.plot(pxi, pfi, label='Polinomio')
    plt.legend()
    plt.xlabel('xi')
    plt.ylabel('fi')
    plt.title('Diferencias Divididas - Newton')
    plt.show()


xi = np.array([50, 60, 65, 75, 80])
fi = np.array([988, 985.7, 980, 974.5, 971.6])

diferenciasDividas(xi, fi)
    