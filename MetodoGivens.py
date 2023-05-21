from math import copysign, hypot

import numpy as np
#Este es mas recomendado usar que el otro de givens

def _givens_rotation_matrix_entries(a, b):
    """Compute matrix entries for Givens rotation."""
    r = hypot(a, b)
    c = a/r
    s = -b/r

    return (c, s)


def givens_rotation(A):
    (num_rows, num_cols) = np.shape(A)
    # Initialize orthogonal matrix Q and upper triangular matrix R.
    Q = np.identity(num_rows)
    R = np.copy(A)
    # Iterate over lower triangular matrix.
    (rows, cols) = np.tril_indices(num_rows, -1, num_cols)
    for (row, col) in zip(rows, cols):
        # Compute Givens rotation matrix and
        # zero-out lower triangular matrix entries.
        if R[row, col] != 0:
            (c, s) = _givens_rotation_matrix_entries(R[col, col], R[row, col])
            G = np.identity(num_rows)
            G[[col, row], [col, row]] = c
            G[row, col] = s
            G[col, row] = -s
            R = np.dot(G, R)
            Q = np.dot(Q, G.T)
            print("---------------------")
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

# Compute QR decomposition using Givens rotation
(Q, R) = givens_rotation(A)
print(" \nsolve \n")
print("-----------------------------------")
# Print orthogonal matrix Q
print(" Q :\n")
print(Q)

print("-----------------------------------")
# Print upper triangular matrix R
print(" R :\n")
print(R)
""" 
b=np.array([2,4,6,8,13],float)
b=np.transpose(b)
solucion = np.dot(np.dot(np.linalg.inv(R),np.transpose(Q)),b)
print("solucion: ",np.round(solucion,decimals=5)) """
