import numpy as np
def Cholesky(a):
  m, n = a.shape
  if (m !=n ):
    # español
    print("La matriz no es cuadrada.")
  else:
    l = np.zeros((n,n))
    s1 = 0
    for j in range(n):
      for k in range(j): s1+=l[j][k]**2
      l[j][j]=np.sqrt(a[j][j]-s1)
      s1=0
      for i in range(j+1,n):
        for k in range(j): s1+=l[i][k]*l[j][k]
        l[i][j]=(a[i][j]-s1)/l[j][j]
        s1=0
    print("La matriz triangular inferior es:")
    print(l)
    print("La matriz triangular superior es:")
    u=np.transpose(l)
    print(u)
    solution(u,l)
    

def solution(u,l):
    m, n = a.shape  
    y = np.zeros(n)
    s3 = 0
    y[0] = b[0]/l[0][0]   
    for k in range(1, n):
        for r in range(k):
            s3 += l[k][r] * y[r]
        y[k] = (b[k]-s3) / l[k][k]
        s3 = 0          
    x = np.zeros(n)
    s4 = 0
    x[n-1] = y[n-1]/u[n-1][n-1]
    for k in range(n-2, -1, -1):
        for r in range(k+1, n):
            s4 += u[k][r] * x[r]
        x[k] = (y[k] - s4)/u[k][k]
        s4 = 0
    for i in range(n):
        print("x" + str(i + 1) + " = ", x[i])
    print("x" " = ", x)

a = np.array([[4,-1,0,-1,0,0],[-1,4,-1,0,-1,0],[0,-1,4,0,0,-1],[-1,0,0,4,-1,0],[0,-1,0,-1,4,-1],[0,0,-1,0,-1,4]],float)
b = np.array([56,25,62,41,10,47])
print("Respuesta:")
Cholesky(a)
