import numpy as np


def CuasiNewton(invA, f, x, tol):
    k = 0
    while np.linalg.norm(f(x)) >= tol:
        s=-1*np.transpose(np.dot(invA,f(x)))
        aux = x
        x = x + s
        y = f(x) - f(aux)
        invA = invA + np.dot(np.transpose(s)-np.dot(invA,y), np.dot(s,invA)) / np.dot(np.dot(s,invA),y)
        k += 1
        print("Para iteracion " + str(k) + " el x es:")
        print(x)
    print("El metodo termino con " + str(k) + " iteraciones")


def f(x):
    x = np.transpose(x)
    ft = np.zeros((2, 1))
    ft[0, 0] = x[0] * x[1] - 42
    ft[1, 0] = (x[0] + 5) * (x[1] + 5) - 132

    return ft


x0 = np.array([3., 4.])
A0 = np.diag([1., 1.])
invA=np.linalg.inv(A0)
CuasiNewton(invA, f, x0, 1E-5)