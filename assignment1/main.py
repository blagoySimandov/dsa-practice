from xcollections.graph import Graph
from timeit import timeit
from prettyplots.runtime import plot_runtime_growth, plot_dijkstra_comparison
from logging import getLogger

import matplotlib.pyplot as plt

logger = getLogger(__name__)


########
## Q3 ##
########


def benchmark_dijkstra_q3(sizes):
    times = []

    for size in sizes:
        logger.info(f"Testing graph size: {size}x{size}")

        g = Graph()
        m = g.generate_random_graph(size, size)

        def dijkstra_wrapper():
            g.dijkstra(m[size // 2][size // 2], m[0][0], False)

        # reduce iterations for larger graphs coz i cant be bothered to wait atm
        iterations = 5
        execution_time = timeit(dijkstra_wrapper, number=iterations)
        avg_time = execution_time / iterations
        times.append(avg_time)

        logger.info(f"Average execution time: {avg_time:.6f} seconds")

    return times


sizes = [25, 100, 200, 300, 400, 500]
execution_times = benchmark_dijkstra_q3(sizes)

plot_runtime_growth(
    sizes=sizes,
    execution_times=execution_times,
    algorithm_name="Dijkstra's Algorithm APQ Implementation",
)


plt.show()

########
## Q4 ##
########


def benchmark_dijkstra_q4():
    grid_size = 500
    center = grid_size // 2

    distances = []
    for d in range(0, 251, 25):
        distances.append(d)

    early_stop_times = []
    all_nodes_times = []
    path_lengths = []

    g = Graph()
    m = g.generate_random_graph(grid_size, grid_size)
    source = m[center][center]

    for d in distances:
        dest_row = center - d
        dest_col = center - d

        dest_row = max(0, dest_row)
        dest_col = max(0, dest_col)

        destination = m[dest_row][dest_col]

        def early_stop_wrapper():
            return g.dijkstra(source, destination, False, early_stop=True)

        def all_nodes_wrapper():
            return g.dijkstra(source, destination, False, early_stop=False)

        iterations = 10

        early_stop_time = timeit(early_stop_wrapper, number=iterations)
        early_stop_avg = early_stop_time / iterations
        early_stop_times.append(early_stop_avg)

        all_nodes_time = timeit(all_nodes_wrapper, number=iterations)
        all_nodes_avg = all_nodes_time / iterations
        all_nodes_times.append(all_nodes_avg)

        path, _ = g.dijkstra(source, destination, False)
        path_lengths.append(len(path))

        logger.info(f"Distance from center: {d} cells")
        logger.info(f"Path length: {len(path)} nodes")
        logger.info(f"Early stop avg time: {early_stop_avg:.6f} seconds")
        logger.info(f"All nodes avg time: {all_nodes_avg:.6f} seconds")
        logger.info(f"Speedup: {all_nodes_avg / early_stop_avg:.2f}x")
        logger.info("-" * 40)

    # Use the prettyplots module for visualization
    plot_dijkstra_comparison(
        distances=distances,
        early_stop_times=early_stop_times,
        all_nodes_times=all_nodes_times,
        path_lengths=path_lengths,
    )

    plt.show()

    return {
        "distances": distances,
        "early_stop_times": early_stop_times,
        "all_nodes_times": all_nodes_times,
        "path_lengths": path_lengths,
    }


benchmark_results = benchmark_dijkstra_q4()


########
## Q5 ##
########
