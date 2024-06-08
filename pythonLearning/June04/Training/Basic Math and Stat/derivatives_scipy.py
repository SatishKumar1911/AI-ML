from scipy.misc import derivative
import numpy as np


def fun(x):
    return x ** 2 + 3 * x + 2


x_val = 4
f_prime = derivative(fun, x_val, dx=1e-6)

print('Derivative: x ** 2 + 3 * x + 2 ', f_prime)

print('-' * 30)


# Define the functions
def g(x):
    return x ** 2


def h(x):
    return 3 * x + 1


# Sum function
def sum_func(x):
    return g(x) + h(x)


# Compute the derivative of the sum at a point, say x=1
x_val = 1
sum_derivative = derivative(sum_func, x_val, dx=1e-6)
print("Sum Function: g(x) + h(x) = x**2 + 3*x + 1")
print(f"Sum Derivative at x = {x_val}: (g + h)'(x) =", sum_derivative)


# Product function
def product_func(x):
    return g(x) * h(x)


# Compute the derivative of the product at a point, say x=1
x_val = 1
product_derivative = derivative(product_func, x_val, dx=1e-6)
print("Product Function: g(x) * h(x) = (x**2) * (3*x + 1)")
print(f"Product Derivative at x = {x_val}: (g * h)'(x) =", product_derivative)


# Quotient function
def quotient_func(x):
    return g(x) / h(x)


# Compute the derivative of the quotient at a point, say x=1
x_val = 1
quotient_derivative = derivative(quotient_func, x_val, dx=1e-6)
print("Quotient Function: g(x) / h(x) = (x**2) / (3*x + 1)")
print(f"Quotient Derivative at x = {x_val}: (g / h)'(x) =", quotient_derivative)

print('-' * 30)


# Define the inner and outer functions
def gs(x):
    return np.sin(x)


def f(u):
    return np.exp(u)


# Composite function


def composite_func(x):
    return f(gs(x))


# Compute the derivative using the chain rule at a point, say x=1
x_val = 1
inner_derivative = derivative(gs, x_val, dx=1)
outer_derivative = derivative(f, gs(x_val), dx=1)
chain_derivative = outer_derivative * inner_derivative
print("Composite Function: f(gs(x)) = exp(sin(x))")
print(f"Chain Rule Derivative at x = {x_val}: dy/dx =", chain_derivative)


# Define the function
def fn(x):
    return np.sin(x)


# Compute the first, second, and third derivatives at a point, say x=1
x_val = 1
f_prime = derivative(fn, x_val, dx=1, n=1, order=3)
f_double_prime = derivative(fn, x_val, dx=1, n=2, order=5)
f_triple_prime = derivative(fn, x_val, dx=1, n=3, order=7)
print("Function: f(x) = sin(x)")
print(f"First Derivative at x = {x_val}: f'(x) =", f_prime)
print(f"Second Derivative at x = {x_val}: f''(x) =", f_double_prime)
print(f"Third Derivative at x = {x_val}: f'''(x) =", f_triple_prime)
