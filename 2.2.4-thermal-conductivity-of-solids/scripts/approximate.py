import numpy as np
from scipy.optimize import minimize


# par[0] = alpha
# par[1] = x0
# equation: exp(alpha * (x - x0)

def fit(f, params, x, y):
    """Аргументы:
        f - функция, которую мы хотим оптимизировать.
        params - начальное состояние параметров, можно просто передать нули,
            главное чтоб их было нужное количество
        x, y - точки, под которые подгоняем функцию
    """
    if len(x) != len(y):
        raise "Иксов должно быть столько же, сколько и игреков"

    def err(par, x_, y_):
        y1 = f(par, x_)
        return np.sum((y1 - y_) ** 2)

    return minimize(err, params, args=(x, y)).x


def line(par, x):
    return par[0] * x + par[1]


def approximate(x_dots, y_dots, eps=50):
    par = np.zeros((2,))
    par = fit(line, par, x_dots, y_dots)
    print(f'y = {par[0]} * x + {par[1]}')

    x = x_dots
    y = line(par, x)

    return x, y
