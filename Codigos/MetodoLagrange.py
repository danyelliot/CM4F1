import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x, y, xi):
    n = len(x)
    result = 0.0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (xi - x[j]) / (x[i] - x[j])
        result += term
    return result

# Definir la función original
def f(x):
    return x**2 / np.sqrt(1 + x**2)

# Definir los puntos de interpolación
x_interpolation = np.linspace(-4, 4, 9)
y_interpolation = f(x_interpolation)

# Definir los puntos para la gráfica
x_plot = np.linspace(-4, 4, 100)
y_exact = f(x_plot)
y_approx = np.array([lagrange_interpolation(x_interpolation, y_interpolation, xi) for xi in x_plot])

# Calcular el error absoluto y el error relativo en cada punto
errors_abs = np.abs(y_exact - y_approx)
errors_rel = np.abs((y_exact - y_approx) / y_exact)

# Calcular el polinomio de interpolación reducido
coefs = np.polyfit(x_interpolation, y_interpolation, len(x_interpolation)-1)
poly_reduced = np.poly1d(coefs)

# Graficar la función exacta y la aproximada
plt.plot(x_plot, y_exact, label='Función exacta')
plt.plot(x_plot, y_approx, label='Interpolación de Lagrange')
plt.scatter(x_interpolation, y_interpolation, color='red', label='Puntos de interpolación')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Interpolación de Lagrange')
plt.legend()
plt.grid(True)
plt.show()

# Imprimir el error absoluto y el error relativo en cada punto
for i in range(len(x_plot)):
    print(f'x = {x_plot[i]:.2f}: Error absoluto = {errors_abs[i]:.6f}, Error relativo = {errors_rel[i]:.6f}')

# Imprimir el polinomio de interpolación reducido
print('Polinomio de interpolación reducido:')
print(poly_reduced)
print()
