import numpy as np
from pstats import Stats
from cProfile import Profile



def interpolate_linear_slow1(x_data, y_data, x):
    y = []
    for x_k in x:
        i = 0
        while i < len(x_data) and x_data[i] < x_k:
            i += 1
        if i == 0:
            i = 1
        elif i == len(x_data):
            i = len(x_data) - 1
        x_lower = x_data[i - 1]
        x_upper = x_data[i]
        y_lower = y_data[i - 1]
        y_upper = y_data[i]
        y_k = (y_upper - y_lower) / (x_upper - x_lower) * (x_k - x_lower) + y_lower
        y.append(y_k)
    return np.array(y)

def interpolate_linear_slow2(x_data, y_data, x):
    n = len(x_data)
    y = []
    for x_k in x:
        i = 0
        while i < n and x_data[i] < x_k:
            i += 1
        if i == 0:
            i = 1
        elif i == n:
            i = n - 1
        x_lower = x_data[i - 1]
        x_upper = x_data[i]
        y_lower = y_data[i - 1]
        y_upper = y_data[i]
        yi = (y_upper - y_lower) / (x_upper - x_lower) * (x_k - x_lower) + y_lower
        y.append(yi)
    return np.array(y)

n_data = 100
rng = np.random.default_rng(42)
x_data = np.sort(rng.uniform(low=0, high=10, size=n_data))
y_data = np.sin(x_data * (10 - x_data)) * np.exp(-x_data / 3)
x = np.linspace(x_data.min(), x_data.max(), 1_000_000)

with Profile() as pr:
    y = interpolate_linear_slow1(x_data, y_data, x)
stats = Stats(pr)
stats.strip_dirs()
stats.sort_stats("cumtime")
stats.print_stats()
