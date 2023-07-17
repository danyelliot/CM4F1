import numpy as np

def F(x):
    # x1 = x[0] , x2 = x[1] , x3 = x[2]
    # f1 = x1**2 + x2 - 37
    f1= x[0]**2 + x[1] - 37
    # f2 = x1 - x2**2 - 5
    f2= x[0] - x[1]**2 - 5
    # f3 = x1 + x2 + x3 - 3
    f3= x[0] + x[1] + x[2] - 3
    return np.array([f1,f2,f3])

def Jacobiano(x):
    # f1 = x1**2 + x2 - 37
    # f2 = x1 - x2**2 - 5
    # f3 = x1 + x2 + x3 - 3
    return np.array([[2*x[0],1,0],[1,-2*x[1],0],[1,1,1]])

if __name__ == "__main__":
    x0 = np.array([0.,0.,1.5])
    Tolerancia = 1e-4
    N = 100
    h = 1/N
    w0 = x0
    print(F(x0))
    for i in range(N):
        print(f"W_{i} = {w0}")
        k1 = h*np.dot(np.linalg.inv(-Jacobiano(w0)),F(x0))
        k2 = h*np.dot(np.linalg.inv(-Jacobiano(w0+0.5*k1)),F(x0))
        k3 = h*np.dot(np.linalg.inv(-Jacobiano(w0+0.5*k2)),F(x0))
        k4 = h*np.dot(np.linalg.inv(-Jacobiano(w0+k3)),F(x0))
        w0 = w0 + (k1+2*k2+2*k3+k4)/6
        print("K_1: ",k1)
        print("K_2: ",k2)
        print("K_3: ",k3)
        print("K_4: ",k4)
        if(np.linalg.norm(k1) < Tolerancia):
            break
    print("x*= ",w0)
    #round 4 decimals with np.round
    print("f(x*)= ",np.round(F(w0),4))
