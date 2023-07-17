import numpy as np
np.set_printoptions(precision=3)

A = np.array([[24, 6 , 12],[-4, 1, -4],[-3, 0, 1]],float)
b = np.array([156,0,0])


x0 = np.zeros(3)
x1 = np.zeros(3)

k = 1
xant = np.copy(x0)



x0[0] = (b[0] - A[0,1] * x0[1] - A[0,2] * x0[2]) / A[0,0]
x0[1] = (b[1] - A[1,0] * x0[0] - A[1,2] * x0[2]) / A[1,1]
x0[2] = (b[2] - A[2,0] * x0[0] - A[2,1] * x0[1]) / A[2,2]

print ('x0                = ', x0)
print ('x0-xant           = ', x0-xant)
print ('max(abs(x0-xant)) = ', max(abs(x0-xant)))

k = 2
xant = np.copy(x0)
x0[0] = (b[0] - A[0,1] * x0[1] - A[0,2] * x0[2]) / A[0,0]
x0[1] = (b[1] - A[1,0] * x0[0] - A[1,2] * x0[2]) / A[1,1]
x0[2] = (b[2] - A[2,0] * x0[0] - A[2,1] * x0[1]) / A[2,2]

print ('x0                = ', x0)
print ('x0-xant           = ', x0-xant)
print ('max(abs(x0-xant)) = ', max(abs(x0-xant)))

k = 3
xant = np.copy(x0)
x0[0] = (b[0] - A[0,1] * x0[1] - A[0,2] * x0[2]) / A[0,0]
x0[1] = (b[1] - A[1,0] * x0[0] - A[1,2] * x0[2]) / A[1,1]
x0[2] = (b[2] - A[2,0] * x0[0] - A[2,1] * x0[1]) / A[2,2]

print ('x0                = ', x0)
print ('x0-xant           = ', x0-xant)
print ('max(abs(x0-xant)) = ', max(abs(x0-xant)))

print ('x0 = ', x0)

x = np.linalg.solve(A,b);
print(x)
print ('error = ', max(abs(x0-x)))