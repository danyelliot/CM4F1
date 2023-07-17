from math import copysign, hypot

import numpy as np
#Este es mas recomendado usar que el otro de givens

def givens_rotation_matrix_entrada(a, b):
    #Matrices de rotacion
    r = hypot(a, b)
    c = a/r
    s = -b/r

    return (c, s)


def givens_rotation(A):
    (num_rows, num_cols) = np.shape(A)
    # Se inicia la matriz ortogonal Q y la tringular superior R
    Q = np.identity(num_rows)
    R = np.copy(A)
    # Iteración sobre la matriz triangular inferior
    (rows, cols) = np.tril_indices(num_rows, -1, num_cols)
    print("Matrices de rotación de Givens")
    for (row, col) in zip(rows, cols):
        # Calculo de la matriz de rotación de Givens
        if R[row, col] != 0:
            (c, s) = givens_rotation_matrix_entrada(R[col, col], R[row, col])
            G = np.identity(num_rows)
            G[[col, row], [col, row]] = c
            G[row, col] = s
            G[col, row] = -s
            R = np.dot(G, R)
            Q = np.dot(Q, G.T)
            print("------------------------------------------")
            print("G",row+1,col+1,"\n")
            print(G)

    return (Q, R)



# Set print options (optional)
np.set_printoptions(precision=8, suppress=True)

# Input matrix
A=np.array([
    [2, 1,1],
    [1, 2,1],
    [1 ,1,1 ]],float)
# Print input matrix
#print(A)

A=np.matrix([
    [1,1,1],
    [12,10,9],
    [2,-1,0]
    ],float)
b=np.matrix([44,436,0],float)
b=np.transpose(b)


# Compute QR decomposition using Givens rotation
(Q, R) = givens_rotation(A)

print("------------------------------------------")
#Matriz ortogonal Q
print(" Q = (G23)(G31)(G32)\n")
print(Q)

print("------------------------------------------")
# Matriz trigular superior R
print(" R = (G32)(G31)(G21)\n")
print(R)
print("------------------------------------------")
print("c = (Q^T)(b)\n")

print(np.dot(np.transpose(Q),b))
solucion = np.dot(np.dot(np.linalg.inv(R),np.transpose(Q)),b)
print("------------------------------------------")

print("Solución x = (R^-1)(Q^T)(b) \n")
print(np.round(solucion,decimals=5))