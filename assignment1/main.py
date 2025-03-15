from xcollections.graph import Graph
from timeit import timeit
from prettyplots.runtime import plot_runtime_growth
from logging import getLogger

import matplotlib.pyplot as plt

logger = getLogger(__name__)


def benchmark_dijkstra(sizes):
    times = []

    for size in sizes:
        logger.info(f"Testing graph size: {size}x{size}")

        g = Graph()
        m = g.generate_random_graph(size, size)

        def dijkstra_wrapper():
            g.dijkstra(m[0][0], m[size - 1][size - 1], True)

        # reduce iterations for larger graphs coz i cant be bothered to wait atm
        iterations = max(1, int(100 / size))
        execution_time = timeit(dijkstra_wrapper, number=iterations)
        avg_time = execution_time / iterations
        times.append(avg_time)

        logger.info(f"Average execution time: {avg_time:.6f} seconds")

    return times


sizes = [50, 100, 200, 300, 400, 500]
execution_times = benchmark_dijkstra(sizes)

plot_runtime_growth(
    sizes=sizes,
    execution_times=execution_times,
    algorithm_name="Dijkstra's Algorithm",
)


plt.show()
