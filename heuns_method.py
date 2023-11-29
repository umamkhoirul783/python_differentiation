import numpy as np

# (a) Simple Heun without Corrector
def heun(x, y, h):
    dy1dx = derivs(x, y)
    ye = y + dy1dx * h
    dy2dx = derivs(x + h, ye)
    slope = (dy1dx + dy2dx) / 2
    ynew = y + slope * h
    x = x + h
    return x, ynew

# (b) Midpoint Method
def midpoint(x, y, h):
    dydx = derivs(x, y)
    ym = y + dydx * h / 2
    dymdx = derivs(x + h / 2, ym)
    ynew = y + dymdx * h
    x = x + h
    return x, ynew

# (c) Heun with Corrector
def heun_with_corrector(x, y, h):
    es = 0.01
    maxit = 20

    dy1dx = derivs(x, y)
    ye = y + dy1dx * h
    iter = 0

    while True:
        yeold = ye
        dy2dx = derivs(x + h, ye)
        slope = (dy1dx + dy2dx) / 2
        ye = y + slope * h
        iter += 1
        ea = np.abs((ye - yeold) / ye) * 100

        if ea <= es or iter > maxit:
            break

    ynew = ye
    x = x + h
    return x, ynew

# Example usage
def derivs(x, y):
    # Replace this with your derivative calculation
    dydx = ...  # Implement the derivative calculation here
    return dydx

# Initial values
x_initial = 0.0
y_initial = 1.0
h = 0.1

# Example usage of each method
x, y_new_heun = heun(x_initial, y_initial, h)
x, y_new_midpoint = midpoint(x_initial, y_initial, h)
x, y_new_heun_corrector = heun_with_corrector(x_initial, y_initial, h)

# Display results
print("Simple Heun without Corrector: x =", x, ", y =", y_new_heun)
print("Midpoint Method: x =", x, ", y =", y_new_midpoint)
print("Heun with Corrector: x =", x, ", y =", y_new_heun_corrector)
