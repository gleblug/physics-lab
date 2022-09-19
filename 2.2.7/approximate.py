import numpy as np


def lessSquaresMethod(x_dots: np.array, y_dots: np.array):
    """
    :param x_dots: X dots
    :param y_dots: Y dots
    :return: Line approximation coefficients with less squares method
    """
    x_dots = np.array(x_dots)
    y_dots = np.array(y_dots)

    if len(x_dots) != len(y_dots):
        raise f"Count of x_dots ({len(x_dots)}) not equal to count of y_dots ({len(y_dots)})"
    n = len(x_dots)

    xy = np.sum(x_dots * y_dots) / n
    x_av = np.sum(x_dots) / n
    y_av = np.sum(y_dots) / n
    x2_av = np.sum(x_dots ** 2) / n

    k = (xy - x_av * y_av) / (x2_av - x_av ** 2)
    b = (y_av - k * x_av)
    # x_matrix = np.stack([x_dots, np.ones(len(x_dots))])
    # k, b = np.linalg.lstsq(x_matrix, y_dots, rcond=0)[0]
    print(f"y = {k} * x + {b}")

    return k, b
