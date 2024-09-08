import sympy as sp
import numpy as np

def sympy_to_pyfunc(expression, symbols):
    f = sp.lambdify(symbols, expression, modules=['numpy'])
    return f

def main():
    # We ask the user to input the differential function as a string
    func_expr = input("Enter the differential function f(x, y): ")

    # We define the symbols that will be used in the differential function
    x, y = sp.symbols('x y')
    func_sympy = sp.sympify(func_expr)  # We convert the string into a sympy expression

    # We use lambdify to convert the sympy expression into a Python function
    f = sympy_to_pyfunc(func_sympy, (x, y))

    # We ask the user to enter the initial conditions and the step size
    x0 = float(input("Enter the initial value of x (x0): "))
    y0 = float(input("Enter the initial value of y (y0): "))
    h = float(input("Enter the step size (h): "))

    # We run the Euler method with the user's inputs
    x_values, y_values = euler_method(f, x0, y0, h)

    # We calculate the absolute error and add it to the table
    absolute_errors = calculate_absolute_errors(y_values)

    # We print the calculated x, y values, and absolute error
    for i in range(len(x_values)):
        print(f"x = {x_values[i]:.4f}, y = {y_values[i]:.4f}, Absolute Error = {absolute_errors[i]:.4f}")

def euler_method(f, x0, y0, h):
    x_values = [x0]
    y_values = [y0]

    # We ask the user to enter the x value up to which they want to calculate the solution
    x_end = float(input("Enter the x value up to which to calculate: "))

    # We perform the Euler method iterations until reaching x_end
    while x_values[-1] < x_end:
        x_n, y_n = x_values[-1], y_values[-1]
        y_next = y_n + h * f(x_n, y_n)
        x_next = x_n + h
        x_values.append(x_next)
        y_values.append(y_next)

    return x_values, y_values

def calculate_absolute_errors(y_values):
    # We calculate the absolute error between the y values and the values in the previous iteration
    absolute_errors = [0.0]  # The first value has no error because there is no previous value to compare to
    for i in range(1, len(y_values)):
        absolute_error = np.abs(y_values[i] - y_values[i - 1])
        absolute_errors.append(absolute_error)

    return absolute_errors

if __name__ == "__main__":
    main()
