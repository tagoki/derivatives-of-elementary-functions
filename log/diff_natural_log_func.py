import sympy as sp 
import numpy as np 
import matplotlib.pyplot as plt
from natural_log_func import f 

x = sp.symbols('x')

df = sp.diff(f, x)

def plot_derivative():
    x_value_for_df = np.linspace(1.1, 20)
    y_value_for_df = []

    for el in x_value_for_df:
        y_value_for_df.append(df.subs(x, el))  # Используем df вместо f для производной
    
    plt.figure(figsize=(5, 6))
    plt.grid(True)
    plt.plot(x_value_for_df, y_value_for_df, 'b-', label='1/x')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График функции y = 1/x (производная от y = ln(x))')
    plt.legend()

if __name__ == '__main__':
    plot_derivative()
    plt.show()