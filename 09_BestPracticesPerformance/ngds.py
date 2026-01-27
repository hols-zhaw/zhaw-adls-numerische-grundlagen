import numpy as np


def interpolate_linear(x_data, y_data, x):
    """
    Perform linear interpolation to estimate the value of a function at a given point.
    Parameters:
        x_data (array-like): A sequence of x-coordinates (must be sorted in ascending order).
        y_data (array-like): A sequence of y-coordinates corresponding to x_data.
        x (array-like): The x-coordinates at which to interpolate.
    Returns:
        float: The interpolated y-coordinate corresponding to the input x.
    Raises:
        AssertionError: If any of the following conditions are not met:
            - x_data and y_data are array-like structures.
            - x_data and y_data have the same length.
            - x_data and y_data contain at least two points.
            - x_data is sorted in ascending order.
            
    Notes:
        - This function assumes that x_data is sorted in ascending order.
        - The interpolation is performed using the formula:
          y = y_data[i] + m[i] * (x - x_data[i]),
          where m[i] is the slope between consecutive points in x_data and y_data.
    """
    assert isinstance(x_data, (np.ndarray, list, tuple)), "x_data must be an array-like structure"
    assert isinstance(y_data, (np.ndarray, list, tuple)), "y_data must be an array-like structure"
    assert isinstance(x, (np.ndarray, list, tuple)), "x must be an array-like structure"
    assert len(x_data) == len(y_data), "x_data and y_data must have the same length"
    assert len(x_data) > 1, "x_data and y_data must have at least two points"
    if not isinstance(x_data, np.ndarray):
        x_data = np.array(x_data)
    if not isinstance(y_data, np.ndarray):
        y_data = np.array(y_data)
    if not isinstance(x, np.ndarray):
        x = np.array(x)
    assert np.all(np.diff(x_data) > 0), "x_data must be sorted in ascending order"
    assert np.all((x_data[0] <= x) & (x <= x_data[-1])), "x must be within the range of x_data"

    i = np.searchsorted(x_data, x) - 1
    i = np.where(i < 0, 0, i)
    m = np.diff(y_data) / np.diff(x_data)
    return y_data[i] + m[i] * (x - x_data[i])


def find_root_bisection(f, a0, b0, xtol=1e-8, ytol=1e-8, maxiter=1000):
    """
    Perform the bisection method to find a root of a continuous function within a given interval.
    Parameters:
        f (callable): The function for which the root is to be found. Must be continuous on the interval [a0, b0].
        a0 (float or int): The lower bound of the interval.
        b0 (float or int): The upper bound of the interval.
        xtol (float, optional): The tolerance for the x-axis (interval width). Default is 1e-8.
        ytol (float, optional): The tolerance for the y-axis (function value). Default is 1e-8.
        maxiter (int, optional): The maximum number of iterations to perform. Default is 1000.
    Returns:
        numpy.ndarray: A 2D array where each row contains:
            - steps (int): The iteration step number.
            - x (float): The midpoint of the current interval.
            - y (float): The function value at the midpoint.
            - Dx (float): Half the width of the current interval.
            - Dy (float): The absolute value of the function at the midpoint.
    Raises:
        AssertionError: If any of the following conditions are not met:
            - `f` is callable.
            - `a0` and `b0` are numbers.
            - `xtol` and `ytol` are positive numbers.
            - `maxiter` is a non-negative integer.
            - `a0` and `b0` are distinct.
            - `f(a0) * f(b0) < 0` (the function values at the interval bounds must have opposite signs).
    Notes:
        The method assumes that the function `f` is continuous on the interval [a0, b0] and that there is at least one root within the interval. The algorithm stops when either the interval width (Dx) is less than `xtol` and the function value (Dy) is less than `ytol`, or the maximum number of iterations (`maxiter`) is reached.
    """
    assert callable(f), "f must be a callable function"
    assert isinstance(a0, (int, float)), "a0 must be a number"
    assert isinstance(b0, (int, float)), "b0 must be a number"
    assert isinstance(xtol, (int, float)), "xtol must be a number"
    assert isinstance(ytol, (int, float)), "ytol must be a number"
    assert isinstance(maxiter, int), "maxiter must be an integer"
    assert a0 != b0, "a0 and b0 must be different numbers"
    assert f(a0) * f(b0) < 0
    assert xtol > 0
    assert ytol > 0
    assert maxiter >= 0

    a, b = (a0, b0) if a0 < b0 else (b0, a0)
    x = (a + b) / 2
    y = f(x)
    ya = f(a)
    Dx = abs(b - a) / 2
    Dy = abs(y)
    steps = 0
    res = [(steps, x, y, Dx, Dy)]

    while (Dx > xtol or Dy > ytol) and steps < maxiter:
        if ya * y < 0:
            b = x
        else:
            a = x
            ya = y
        x = (a + b) / 2
        y = f(x)
        Dx = abs(b - a) / 2
        Dy = abs(y)
        steps += 1
        res.append((steps, x, y, Dx, Dy))

    return np.array(res)
