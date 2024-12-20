import numpy as np

def ddx_FD(function, xi, h):
    dfdx = (function(xi+h) - function(xi))/h
    return dfdx

def ddx_BD(function, xi, h):
    dfdx = (function(xi)-function(xi-h))/h
    return dfdx

def ddx_CD(function, xi, h):
    dfdx = (function(xi+h)-function(xi-h))/(2*h)
    return dfdx

def d2dx2_CD(function, xi, h):
    d2fdx2 = (function(xi+h) - (2*function(xi)) + (function(xi-h)))/(h**2)
    return d2fdx2


h_values = [0.1, 0.0001]

# Function 1: f(x) = sin(x)
f1 = np.sin
xi1 = np.pi/3  # Point to evaluate
actual_f1_prime = np.cos(xi1)  # True value of f'(π/3)
actual_f1_double_prime = -np.sin(xi1)  # True value of f''(π/3)
    
print("f(x) = sin(x) at x = π/3:")
for h in h_values:
    f1_prime_fd = ddx_FD(f1, xi1, h)
    f1_prime_bd = ddx_BD(f1, xi1, h)
    f1_prime_cd = ddx_CD(f1, xi1, h)
    f1_double_prime_cd = d2dx2_CD(f1, xi1, h)

    print(f"h = {h}:")
    print(f"Forward difference f' ≈ {f1_prime_fd}, Relative Error: {abs((f1_prime_fd - actual_f1_prime)/actual_f1_prime)}")
    print(f"Backward difference f' ≈ {f1_prime_bd}, Relative Error: {abs((f1_prime_bd - actual_f1_prime)/actual_f1_prime)}")
    print(f"Central difference f' ≈ {f1_prime_cd}, Relative Error: {abs((f1_prime_cd - actual_f1_prime)/actual_f1_prime)}")
    print(f"Central difference f'' ≈ {f1_double_prime_cd}, Relative Error: {abs((f1_double_prime_cd - actual_f1_double_prime)/abs(actual_f1_double_prime))}")

print("---------------------------------------------------")

# Function 2: f(x) = x^3 - 4x^2 + 1
f2 = lambda x: x**3-4*x**2+1
xi2 = 1  # Point to evaluate
actual_f2_prime = 3*xi2**2-8*xi2  # True value of f'(1)
actual_f2_double_prime = 6*xi2-8  # True value of f''(1)
    
print("f(x) = x^3 - 4x^2 + 1 at x = 1:")
for h in h_values:
    f2_prime_fd = ddx_FD(f2, xi2, h)
    f2_prime_bd = ddx_BD(f2, xi2, h)
    f2_prime_cd = ddx_CD(f2, xi2, h)
    f2_double_prime_cd = d2dx2_CD(f2, xi2, h)

    print(f"h = {h}:")
    print(f"Forward difference f' ≈ {f2_prime_fd}, Relative Error: {abs((f2_prime_fd - actual_f2_prime)/actual_f2_prime)}")
    print(f"Backward difference f' ≈ {f2_prime_bd}, Relative Error: {abs((f2_prime_bd - actual_f2_prime)/actual_f2_prime)}")
    print(f"Central difference f' ≈ {f2_prime_cd}, Relative Error: {abs((f2_prime_cd - actual_f2_prime)/actual_f2_prime)}")
    print(f"Central difference f'' ≈ {f2_double_prime_cd}, Relative Error: {abs((f2_double_prime_cd - actual_f2_double_prime)/abs(actual_f2_double_prime))}")


    