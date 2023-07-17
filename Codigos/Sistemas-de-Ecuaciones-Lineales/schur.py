import numpy as np

def schur_decomposition(A):
    n = len(A)
    Q = np.eye(n)
    T = np.copy(A)

    for k in range(n-1):
        # Obtener la reflexión de Householder
        v = T[k+1:, k]
        s = np.sign(v[0])
        s = 1 if s == 0 else s
        v[0] += s * np.linalg.norm(v)
        v = v / np.linalg.norm(v)

        # Actualizar la matriz T y la matriz de transformación Q
        T[k+1:, k:] -= 2 * np.outer(v, np.dot(v, T[k+1:, k:]))
        T[:, k+1:] -= 2 * np.outer(np.dot(T[:, k+1:], v), v.T)
        Q[k+1:, :] -= 2 * np.outer(v, np.dot(v, Q[k+1:, :]))

    return Q.T, T

# Ejemplo de uso
A = np.array([[3, 1, 2], [4, 7, 1], [5, 6, 2]])
Q, T = schur_decomposition(A)
print("Q:\n", Q)
print("T:\n", T)

# Verificación
print("Q * T * Q^T:\n", np.dot(np.dot(Q, T), Q.T))
