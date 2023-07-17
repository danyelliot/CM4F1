import numpy as np

def autovalores(A, eps=1e-6, max_iter=1000):
    n = A.shape[0]
    X = np.eye(n)
    eigenvalues = np.zeros(n)
    iterations = 0
    converged = False
    
    while not converged and iterations < max_iter:
        B = A - eigenvalues[0] * np.eye(n)
        for i in range(1, n):
            B[i,i] -= eigenvalues[i]
        
        try:
            Q, R = np.linalg.qr(B)
            X = np.dot(X, Q)
        except np.linalg.LinAlgError:
            break
        
        eigenvalues_old = np.copy(eigenvalues)
        for i in range(n):
            eigenvalues[i] = np.dot(X[:,i], A.dot(X[:,i])) / np.dot(X[:,i], X[:,i])
        
        if np.allclose(eigenvalues, eigenvalues_old, atol=eps, rtol=0):
            converged = True
        
        iterations += 1
    
    eigenvectors = X / np.linalg.norm(X, axis=0)
    
    return eigenvalues, eigenvectors


A = np.array([[0.7,-0.1,-0.2],[-0.2,0.8,-0.5],[-0.3,-0.3,0.9]]).astype(float)
eigenvalues, eigenvectors = autovalores(A, eps=1e-6)
print("Autovalores:", eigenvalues)
print("Autovectores:\n", eigenvectors)
