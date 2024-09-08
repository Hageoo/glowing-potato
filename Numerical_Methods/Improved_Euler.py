import sympy as sp
import numpy as np
import pandas as pd

def euler_method(func, x0, y0, xf, h):
    # Calculates the number of steps needed to cover the interval from x0 to xf
    n = int(np.ceil((xf - x0) / h))
    # Creates an array of equally spaced x points in the given interval
    x = np.linspace(x0, x0 + n * h, n+1)
    # Initializes an array y with zeros and sets the initial value y0
    y = np.zeros(n+1)
    y[0] = y0

    # Implements Euler's method to approximate the solution of the differential equation
    for i in range(n):
        f1 = func(x[i], y[i])  # Calculates the derivative at the current point
        y_pred = y[i] + h * f1  # Calculates a temporary value for y
        f2 = func(x[i] + h, y_pred)  # Calculates the derivative at the predicted point
        y[i+1] = y[i] + h * (f1 + f2) / 2  # Updates y[i+1] using the weighted average of f1 and f2

    return x, y

# Converts a string that describes a mathematical operation into a Python function
def string_to_func(string):
    def func(x, y):
        return eval(string)
    return func

# Saves the results to a CSV file, including a column for the absolute value of 'y'
def save_to_csv(x, y, filename):
    # Creates a Pandas DataFrame with the columns 'x', 'y', and 'abs_y' (absolute value of 'y')
    df = pd.DataFrame({'x': x, 'y': y, 'abs_y': np.abs(y)})
    # Saves the DataFrame to a CSV file without including indices
    df.to_csv(filename, index=False)

def main():
    # Prompts the user for the differential equation, initial values, final value of x, step size, and CSV filename
    ecuacion = input("Enter the differential equation dy/dx in terms of x and y: ")
    x0 = float(input("Initial value of x: "))
    y0 = float(input("Initial value of y: "))
    xf = float(input("Final value of x: "))
    h = float(input("Step size: "))
    csv_filename = input("CSV filename to save the results: ")

    # Converts the string into a Python function
    func = string_to_func(ecuacion)
    # Solves the differential equation using Euler's method
    x, y = euler_method(func, x0, y0, xf, h)

    # Prints the results
    for i in range(len(x)):
        print(f"x = {x[i]:.6f}, y = {y[i]:.6f}")

    # Saves the results to a CSV file, including a column for the absolute value of 'y'
    save_to_csv(x, y, csv_filename)
    print(f"The results have been saved to {csv_filename}")

if __name__ == "__main__":
    main()
