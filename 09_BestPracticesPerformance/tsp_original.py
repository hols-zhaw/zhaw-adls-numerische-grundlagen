import numpy as np
import matplotlib.pyplot as plt
from itertools import permutations

from pstats import Stats
from cProfile import Profile


def distance(city1, city2):
    """Compute the Euclidean distance between two cities."""
    return np.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)


def total_distance(cities, sequence):
    """Compute the total distance to visit all the cities in the given sequence."""
    total = 0
    for i in range(len(sequence) - 1):
        total += distance(cities[sequence[i]], cities[sequence[i + 1]])
    return total + distance(cities[sequence[-1]], cities[sequence[0]])


def traveling_salesman_brute_force(cities):
    """Find the shortest path to visit all the cities exactly once by brute force."""
    min_distance = np.inf
    min_sequence = None
    for sequence in permutations(range(len(cities))):
        d = total_distance(cities, sequence)
        if d < min_distance:
            min_distance = d
            min_sequence = sequence
    return min_sequence, min_distance


def generate_cities(n, seed=12345):
    """Generate n random city coordinates."""
    rng = np.random.default_rng(seed)
    cities = []
    for _ in range(n):
        cities.append((rng.uniform(-1, 1), rng.uniform(-1, 1)))
    return cities


def plot_path(cities, sequence, min_distance):
    """Plot the path that visits the cities in the given sequence."""
    nodes = [cities[i] for i in sequence]
    nodes.append(nodes[0])
    x, y = np.array(nodes).T
    plt.plot(x, y)
    plt.plot(x, y, "ko")
    for i, city in enumerate(cities):
        plt.annotate(
            str(i),
            city,
            textcoords="offset points",
            xytext=(0, 5),
            ha="center",
            va="bottom",
            annotation_clip=False,
        )
    plt.axis("square")
    plt.xlim(-1.05, 1.05)
    plt.ylim(-1.05, 1.05)
    plt.grid()
    plt.title(f"path={sequence}, dist={min_distance:.3f}")
    plt.show()


if __name__ == "__main__":
    n_cities = 9
    cities = generate_cities(n_cities)

    with Profile() as pr:
        shortest_path, min_distance = traveling_salesman_brute_force(cities)

    stats = Stats(pr)
    stats.strip_dirs()
    stats.sort_stats("cumtime")
    stats.print_stats()

    plot_path(cities, shortest_path, min_distance)
