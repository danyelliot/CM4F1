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
    x0 = np.array([0.,0.,0.])
    Tolerancia = 1e-4
    N = 2
    h = 1/N
    w0 = x0
    print("F(x^(0)) = ",F(x0),"\n")
    for i in range(N):
        print(f"W_{i} = {w0}")
        k1 = h*F(w0)
        k2 = h*F(w0+0.5*k1)
        w0 = (k1 + 2*k2)/6
        print("K_1: ",k1)
        print("K_2: ",k2)
        if(np.linalg.norm(k1) < Tolerancia):
            break
    print("x*= ",w0)
    #round 4 decimals with np.round
    print("f(x*)= ",np.round(F(w0),4))
