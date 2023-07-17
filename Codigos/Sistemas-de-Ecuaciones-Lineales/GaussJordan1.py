import numpy as np  


def GAUSSJORDAN(AB):
    casicero = 1e-15  # Considerar como 0
    tamano = np.shape(AB)
    n = tamano[0]
    m = tamano[1]
    for i in range(0, n - 1, 1):
        columna = abs(AB[i:, i])
        dondemax = np.argmax(columna)
        if (dondemax != 0):
            temporal = np.copy(AB[i, :])
            AB[i, :] = AB[dondemax + i, :]
            AB[dondemax + i, :] = temporal
    for i in range(0, n - 1, 1):
        pivote = AB[i, i]
        adelante = i + 1
        for k in range(adelante, n, 1):
            factor = AB[k, i] / pivote
            AB[k, :] = AB[k, :] - AB[i, :] * factor
    ultfila = n - 1
    ultcolumna = m - 1
    for i in range(ultfila, 0 - 1, -1):
        pivote = AB[i, i]
        atras = i - 1
        for k in range(atras, 0 - 1, -1):
            factor = AB[k, i] / pivote
            AB[k, :] = AB[k, :] - AB[i, :] * factor
        AB[i, :] = AB[i, :] / AB[i, i]
    AB=np.round(AB, decimals = 4)
    return AB

A = np.array([[1,0,0,-3,-5,0,0],[0,1,0,-8,-4,0,0],[0,0,1,-2,-6,0,0],[0,0,0,1,0,-7,-8],[0,0,0,0,1,-6,-2],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1]])
b = np.array([[5],[0],[10],[5],[2],[3],[4]])

AB = np.concatenate((A, b), axis=1)
print(GAUSSJORDAN(AB))



















#calculo de una solucion aproximada con transformaciones de gausss jordan 
#formula 

# 1. se ordena la matriz de mayor a meno
# 2. se divide la fila entre el pivote
# 3. se hace cero los elementos de la columna del pivote
# 4. se repite el proceso hasta que se llegue a la matriz identidad
# 5. se redondea la matriz a 4 decimales
