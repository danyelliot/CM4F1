import math
import numpy as np

def gradienteConjugado(A, B, tol):
    x = np.transpose([-5.05, 80.05, 0])
    r = B
    d = (np.linalg.norm(r))**2
    k = 1
    while math.sqrt(d) > tol * np.linalg.norm(B) and k <= 100:
        if k == 1:
            p = r
        else:
            b = d / auxD2
            p = r + b * p
        w = np.dot(A, p)
        a = d / (np.dot(np.transpose(p), w))
        x = x + a * p
        r = r - a * w
        auxD2 = d
        d = (np.linalg.norm(r))**2
        print(x)
        k += 1

tol = 1.0e-5
A = np.array([[0,0,1], [64,8,1], [256,16,1]], dtype='double')
b = np.array([0,320,0], dtype="double")
gradienteConjugado(A, b, tol)


