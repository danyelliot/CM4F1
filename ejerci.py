import numpy as np
x1=np.array([[0, 5,10,15,20,25,30,0, 5,10,15,20,25,30,0, 5,10,15,20,25,30]]).T
x2=np.array([[0, 0,0,0,0,0,0,10, 10,10,10,10,10,10,20, 20,20,20,20,20,20]]).T
y=np.array([[14.6,12.8,11.3,10.1,9.09,8.26,7.56,
             12.9,11.3,10.1,9.03,8.17,7.46,6.85,
             11.4,10.3,8.96,8.08,7.35,6.73,6.20]]).T
A=np.concatenate((x1*3,x1*2,x1*1,x2,np.ones_like(1,shape=(21,1))),1)
print("Tenemos que la matriz A formada es")
print(A)
print("Formando el sistema A.T @A = A.T@b")
print("A.T @A")
print(A.T@A)
print("A.T @b")
print(A.T@y)
print("Solucion")
r=np.linalg.solve(A.T@A,A.T@y)
print(np.linalg.solve(A.T@A,A.T@y))