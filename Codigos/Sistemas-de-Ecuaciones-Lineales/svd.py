import numpy as np

A = np.array([[4, 11, 14], [8, 7, -2]])

import numpy as np

# Definir matriz A
A = np.array([[4, 11, 14], [8, 7, -2]])

# Calcular matrices U, sigma, Vt
AtA = np.dot(A.T, A)
eig_vals, eig_vecs = np.linalg.eig(AtA)
sigma = np.sqrt(eig_vals)
sigma_inv = np.zeros_like(AtA)
for i in range(len(sigma)):
    if sigma[i] != 0:
        sigma_inv[i, i] = 1/sigma[i]
U = np.dot(np.dot(A, eig_vecs), sigma_inv)
U = np.round(U, 4)
sigma = np.round(sigma, 4)

Vt = eig_vecs.T
Vt = np.round(Vt, 4)

# Imprimir resultados
print("Matriz A:\n", A)
print("Matriz U:\n", U)
print("Vector singular sigma:\n", sigma)
print("Matriz V transpuesta:\n", Vt)

# Verificar descomposición SVD
A_reconstructed = np.dot(U, np.dot(np.diag(sigma), Vt))
A_reconstructed = np.round(A_reconstructed, 2)
print("Matriz A reconstruida:\n", A_reconstructed)



'''
Este código utiliza los siguientes pasos para obtener la descomposición SVD:

Se calcula la matriz A^T A.
Se encuentran los autovalores y autovectores de A^T A.
Los autovalores se ordenan de mayor a menor y los autovectores se reordenan en consecuencia.
Se calcula la matriz diagonal de valores singulares a partir de los autovalores.
Se calcula la matriz de inversa de valores singulares.
Se calcula la matriz U a partir de la matriz A, los autovectores y la matriz de inversa de valores singulares.
Se imprime la descomposición SVD en términos de U, Sigma y la matriz transpuesta de los autovectores.
'''