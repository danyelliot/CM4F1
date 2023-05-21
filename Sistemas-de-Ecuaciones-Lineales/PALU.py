import numpy as np

def LU_decomposition(A):
    n = len(A)
    L = np.eye(n)
    P = np.eye(n)
    U = np.copy(A)

    for i in range(n-1):
        pivot = i
        for j in range(i+1, n):
            if abs(U[j,i]) > abs(U[pivot,i]):
                pivot = j

        if pivot != i:
            U[[i,pivot],:] = U[[pivot,i],:]
            P[[i,pivot],:] = P[[pivot,i],:]
            L[[i,pivot],:i] = L[[pivot,i],:i]
        
        for j in range(i+1, n):
            L[j,i] = U[j,i] / U[i,i]
            U[j,i:] = U[j,i:] - L[j,i] * U[i,i:]
    L = np.round(L, 3)

    return P, L, U

A = np.array([[625,125,25,5,1],[256,64,16,4,1],[81,27,9,3,1],[16,8,4,2,1],[1,1,1,1,1]], float)
b = np.array([225,100,36,9,1], float)
P, L, U = LU_decomposition(A)
print("P:\n", P)
print("L:\n", L)
# imprimir U sin notación científica
np.set_printoptions(suppress=True)
U = np.round(U, 3)
print("U:\n", U)

# solve Ax = b
print("x:\n", np.linalg.solve(A, b))

print((115/77)-(-4.629*(-14/77)))

# Verificar si la descomposición LU es correcta
A_calculada = np.dot(L, U)
print("Matriz A original:\n", A)
print("Matriz A calculada como LU:\n", A_calculada)

'''

print("--------------------")

z = np.linalg.solve(L, b)
print("solucion",np.linalg.solve(U, z))


'''