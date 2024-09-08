import sympy as sp
import pandas as pd

def newton_raphson(func, x0, tol=0.0000001, max_iter=100): 
    # Define the symbol 'x' for the equation
    x = sp.symbols("x")
    # Convert the input string expression into a sympy expression
    expr = sp.sympify(func)
    # Convert the sympy expression into a Python function for numerical evaluation
    f = sp.lambdify(x, expr)
    # Calculate the derivative of the function
    df = sp.diff(expr, x)
    # Convert the derivative expression into a Python function
    df = sp.lambdify(x, df)

    # Lists to store the values of x, f(x), f'(x), and the absolute error for each iteration
    x_values = []
    f_values = []
    df_values = []
    error_values = []

    # Start the iteration process for Newton-Raphson method
    for i in range(max_iter):
        # Update the x value using the Newton-Raphson formula
        x1 = x0 - f(x0) / df(x0)

        # Append the new values to their respective lists
        x_values.append(x1)
        f_values.append(f(x1))
        df_values.append(df(x0))
        error_values.append(abs(f(x0)))

        # Print the iteration details
        print(f"Iteration {i + 1}: x(n+1) = {x1}, x(n) = {x0}, f(x) = {f(x1)}, f'(x_n) = {df(x0)}, Absolute Error = {abs(f(x0))}")

        # Check if the solution has converged based on the tolerance
        if abs(f(x0)) < tol:
            print(f"Convergence reached. Solution: {x1}")
            # Create a DataFrame to store the results
            df_result = pd.DataFrame({'x(n+1)': x_values, 'x(n)': x0, 'f(x)': f_values, "f'(x_n)": df_values, 'Absolute Error': error_values})
            # Save the results to a CSV file
            df_result.to_csv('resultados_newton_raphson.csv', index=False)
            # Return the solution and the lists of values
            return x1, x_values, f_values, df_values, error_values

        # Update the value of x0 for the next iteration
        x0 = x1

    # If the method does not converge after max_iter iterations, print a message
    print("The Newton-Raphson method did not converge after", max_iter, "iterations.")
    # Return None and the lists of values
    return None, x_values, f_values, df_values, error_values

# Example usage:
funcion = "exp(-x)-log(x)"  # Define the function to solve
punto_inicial = 1.3  # Define the initial guess for x
resultado, _, _, _, _ = newton_raphson(funcion, punto_inicial)


