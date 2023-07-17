import numpy as np
def GaussSeidel (A,b,tol = 1.E-4,kmax = 13):
    x0 = np.array([4,4,5],float)
    x1=x0.copy()
    n=len(x0)
    k=0
    while k < kmax :  
        for i in range(n):
            s1 = 0
            s2 = 0
            for j in range(n):
                if j <= i-1:
                    s1 += A[i][j]*x0[j] 
                if j>=i+1:
                    s2+=A[i][j]*x1[j]   
            x0[i] = (b[i]-s2-s1 )/ A[i][i] 
        error = np.linalg.norm(x0 - x1, np.inf) / np.linalg.norm(x0, np.inf)
        print("Para la iteración " + str(k + 1) + ": X = " + str(np.transpose(x0.round(7))) + "\tError: " + str(abs(error)))
        x1 = np.copy(x0)  
        k += 1
    if error <= tol:
            print("Converge ")
    else:
        print("No converge")   

A = np.array([[9,8,9],[5,10,4],[2,4,8]],dtype='double')
b = np.array([170,117,98])
GaussSeidel(A,b)