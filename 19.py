import numpy as np
from numpy.linalg.linalg import solve

def vandermonde(x):
    a = np.zeros((4,4))
    for i in range(0, 4):
        a[:,i] = np.transpose([x[0]**i, x[1]**i, x[2]**i, x[3]**i])

    return a

x0 = np.array([[0, 5, 10, 15]]).T
A = vandermonde(x0)
b1 = np.array([[72.8, 74.2, 75.2, 76.4]]).T
b2 = np.array([[70.23, 70.2, 70.3, 71.2]]).T
s1 = solve(A,b1)
s2 = solve(A,b2)
print("Europa Oeste")
print(f'a0 = {s1[0,0]:<8.5f} a1 = {s1[1,0]:<8.5f} a2 = {s1[2,0]:<8.5f} a3 = {s1[3,0]:<8.5f}\n')
print("Europa Este")
print(f'a0 = {s2[0,0]:<8.5f} a1 = {s2[1,0]:<8.5f} a2 = {s2[2,0]:<8.5f} a3 = {s2[3,0]:<8.5f}\n')

f = lambda x: s1[0,0] + s1[1,0]*x + s1[2,0]*x**2 + s1[3,0]*x**3
g = lambda x: s2[0,0] + s2[1,0]*x + s2[2,0]*x**2 + s2[3,0]*x**3
print(f'Periodo\t 1997\t\t 1983\t\t 1989')
print(f'EUOeste\t{f(2):<8.5f}\t{f(8):<8.5f}\t{f(14):<8.5f}')
print(f'EUEste\t{g(2):<8.5f}\t{g(8):<8.5f}\t{g(14):<8.5f}')

