import numpy as np
import matplotlib.pyplot as plt
from itertools import permutations

from pstats import Stats
from cProfile import Profile


def traveling_salesman_brute_force(cities):
    """Find the shortest path to visit all the cities exactly once by brute force."""
    cities = np.array(cities)
    n_cities = cities.shape[0]
    # Generate all permutations of city indices
    sequences = np.array(list(permutations(range(n_cities))))
    # Greate all possible paths
    paths = cities[sequences]
    # Compute the vectors between consecutive cities
    diffs = np.diff(paths, axis=1)
    # Compute the distances between consecutive cities
    distances = np.linalg.norm(diffs, axis=2)
    # Compute the distance to return to the starting city
    return_distances = np.linalg.norm(paths[:, 0] - paths[:, -1], axis=1)
    # Compute the total lengths of each path
    lengths = np.sum(distances, axis=1) + return_distances
    # Find the minimum length and corresponding sequence
    min_index = np.argmin(lengths)
    min_length = lengths[min_index]
    min_sequence = sequences[min_index]
    return min_sequence, min_length


def generate_cities(n, seed=12345):
    """Generate n random city coordinates."""
    rng = np.random.default_rng(seed)
    return rng.uniform(-1, 1, (n, 2))


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
