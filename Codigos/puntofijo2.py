from math import sqrt

"""
[ f(x) = g(x) - x = 0 ]  ==> x = g(x), x es punto fijo de g
punto_fijo = 1.365230013
print(abs(g_1(punto_fijo) - punto_fijo))
"""


def fixed_point(f, x0, eps = 1e-5, max_iteraciones = 20):
    """Paso 1"""
    i = 0
    """Paso 2"""
    while i < max_iteraciones:
        """Paso 3"""
        f0 = f(x0)
        print(f"x0: {x0}\t f(x0): {f0}")
        """Paso 4"""
        if abs(f0 - x0) < eps:
            print(f"Converge porque |f(x_0) - x_0| = {abs(f0 - x0)} < {eps}")
            break
        """Paso 5"""
        i = i + 1
        """Paso 6"""
        x0 = f0
        print(f"Solution: c = {x0}")
        print(f"Numero de iteraciones: {i}")

'''
g_1 = lambda x: x - x**3 - 4 * x**2 + 10
g_2 = lambda x: sqrt(10 / x - 4 * x)
g_3 = lambda x: 1 / 2 * sqrt(10 - x**3)
g_4 = lambda x: sqrt(10 / (4 + x))
g_5 = lambda x: x - (x**3 + 4 * x**2 - 10) / (3 * x**2 + 8 * x)
'''
g_1 = lambda x,y,z: x**2 - x + y**2 + z**2 - 5
g_2 = lambda x,y,z: x**2 + y**2 - y + z**2 -4
g_3 = lambda x,y,z: x**2 + y**2 + z**2 + z - 6

if __name__ == "__main__":
  fixed_point(f=g_3, x0=1.5)