import numpy as np
import matplotlib.pyplot as plt

#B-splines

x=np.array([2007, 2008, 2009, 2010, 2011, 2012])
y=np.array([133.5, 132.2, 138.7, 141.5, 137.6, 144.2])
n=len(x)-1
h=np.zeros(n)
for i in range (0,n):
    h[i]=x[i+1]-x[i]
u=np.zeros(n-1)
l=np.zeros(n-1)
for i in range (0,n-1):
    u[i]=h[i]/(h[i]+h[i+1])
    l[i]=1-u[i]
d=np.zeros(n-1)
for i in range(1,n-2):
    d[i]=3*(l[i-1]*(y[i+2]-y[i+1])/h[i+1]+u[i-1]*(y[i+1]-y[i])/h[i])    
d[0]=3*(l[0]*(y[1]-y[0])/h[0]\
        +u[0]*(y[2]-y[1])/h[1])-l[0]*0.8# 0.8 y 0.2 son condiciones de frontera de soporte fijo
d[n-2]=3*(l[n-2]*(y[n-1]-y[n-2])/h[n-2]\
            +u[n-2]*(y[n]-y[n-1])/h[n-1])-l[n-2]*0.2
print(d)
A=np.zeros([n-1,n-1])
for i in range(1,n-2):
    A[i,i-1]=l[i-1]
    A[i,i]=2
    A[i,i+1]=u[i]
A[0,0]=A[n-2,n-2]=2
A[0,1]=u[0]
A[n-2,n-3]=l[n-2]
print(A)
M0=np.array(n)
M0=np.linalg.solve(A,d)
M=np.zeros(n+1)
for i in range(1,n):
    M[i]=M0[i-1]
M[0]=0.8
M[n]=0.2
print(M)
#Dibujo
for i in range(0,n):
    x0=np.linspace(x[i],x[i+1],10000)
    y0=y[i]*((x0-x[i+1])**2)*(h[i]+2*(x0-x[i]))/(h[i]**3)\
        +y[i+1]*((x0-x[i])**2)*(h[i]+2*(x[i+1]-x0))/(h[i]**3)\
        +M[i]*((x0-x[i+1])**2)*(x0-x[i])/(h[i]**2)\
        +M[i+1]*((x0-x[i])**2)*(x0-x[i+1])/(h[i]**2)
    plt.plot(x0,y0,color='red')
plt.plot(x0,y0,color='red',label = u"Interpolación de splines cúbicos")
plt.plot(x,y,marker='+',mec='r',mfc='w',label = u"Primitivo")
plt.title("Interpolación de splines cúbicos")
plt.legend()
plt.show()