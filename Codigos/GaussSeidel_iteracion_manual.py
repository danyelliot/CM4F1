import numpy as np

A = np.array([[0.3, -0.3, 0.2], [-0.3, 0.1, 0.1], [1, 0, -1]], dtype="double" )
b = np.array([0, 0, -100])
x1 = np.zeros(3)

# 1era iteracion
print('\nIteracion 1 \n')
k = 1
x0 = np.copy(x1)
x1[0] = (b[0] - A[0,1] * x1[1] - A[0,2] * x1[2]) / A[0,0]
x1[1] = (b[1] - A[1,0] * x1[0] - A[1,2] * x1[2]) / A[1,1]
x1[2] = (b[2] - A[2,0] * x1[0] - A[2,1] * x1[1]) / A[2,2]

print('x1 = ', x1)
print('x1-x0 = ', x1 - x0)
print(' max| x1-x0 | = ', max(abs(x1 - x0)))

# 2da iteracion
print('\nIteracion 2 \n')
k = 2
x0 = np.copy(x1)
x1[0] = (b[0] - A[0,1] * x1[1] - A[0,2] * x1[2]) / A[0,0]
x1[1] = (b[1] - A[1,0] * x1[0] - A[1,2] * x1[2]) / A[1,1]
x1[2] = (b[2] - A[2,0] * x1[0] - A[2,1] * x1[1]) / A[2,2]

print('x1 = ', x1)
print('x1-x0 = ', x1 - x0)
print(' max| x1-x0 | = ', max(abs(x1 - x0)))

# 3ra iteración
print('\nIteracion 3 \n')
k = 3
x0 = np.copy(x1)
x1[0] = (b[0] - A[0,1] * x1[1] - A[0,2] * x1[2]) / A[0,0]
x1[1] = (b[1] - A[1,0] * x1[0] - A[1,2] * x1[2]) / A[1,1]
x1[2] = (b[2] - A[2,0] * x1[0] - A[2,1] * x1[1]) / A[2,2]

print('x1 = ', x1)
print('x1-x0 = ', x1 - x0)
print(' max| x1-x0 | = ', max(abs(x1 - x0)))

# 4ta iteracion

print('\nIteracion 4 \n')
k = 4
x0 = np.copy(x1)
x1[0] = (b[0] - A[0, 1] * x0[1] - A[0, 2] * x0[2]) / A[0, 0]
x1[1] = (b[1] - A[1, 0] * x0[0] - A[1, 2] * x0[2]) / A[1, 1]
x1[2] = (b[2] - A[2, 0] * x0[0] - A[2, 1] * x0[1]) / A[2, 2]

print('x1 = ', x1)
print('x1-x0 = ', x1 - x0)
print('max| x1-x0 | = ', max(abs(x1 - x0)))


x = np.linalg.solve(A,b);
print(x)
print ('error = ', max(abs(x1-x)))