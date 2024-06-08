# Question 3: Calculus with SciPy
#
# Define the function f(x) = x^3 + 2x^2 + x + 1.
# Compute the first and second derivatives of f(x) at x = 1.
# Compute the definite integral of f(x) from x = 0 to x = 2.

from scipy.misc import derivative
import sympy as sp


def f(x):
    return (x ** 3) + (2 * (x ** 2)) + (x + 1)


x_value = 1
f_prime = derivative(f, x_value, dx=1e-6)
f_double_prime = derivative(f, x_value, dx=1e-6, n=2)
print('f_prime:', f_prime)
print('f_double_prime:', f_double_prime)


# Compute the definite integral from 0 to 2
x = sp.symbols('x')
f = (x ** 3) + (2 * (x ** 2)) + (x + 1)
low, high = 0, 2
def_integral = sp.integrate(f, (x, low, high))
print(f"Definite integral of f(x) = x ** 3 + 2 * (x ** 2) + x + 1 from {low} to {high}:")
sp.pprint(def_integral)
