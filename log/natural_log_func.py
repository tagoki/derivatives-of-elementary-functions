import matplotlib.pyplot as plt
import sympy as sp 
import numpy as np

x = sp.symbols('x') #При помощи бибилиотеки sympy мы создаем символьную переменную x

f = sp.log(x) #При помощи бибилиотеки sympy мы создаем функцию f(x) = ln(x)

def plot_log_function():
    x_value_for_log_func = np.linspace(0.1, 20, 100) 
    y_value_for_log_func = [] 

    for el in x_value_for_log_func:
        y_value_for_log_func.append(f.subs(x, el))

    # Создаем график
    plt.figure(figsize=(10, 6))
    plt.plot(x_value_for_log_func, y_value_for_log_func, 'b-', label='ln(x)')
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График функции y = ln(x)')
    plt.legend()

if __name__ == '__main__':
    plot_log_function()
    plt.show()
    
