import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from xcollections.graph import Graph
from timeit import timeit
from prettyplots.runtime import (
    plot_runtime_growth,
    plot_dijkstra_comparison,
    plot_apq_comparison,
    plot_algorithms_comparison,
    plot_multiple_apq_comparison,
)
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def run_q3():
    logger.info(
        "Running Q3: Evaluating runtime of Dijkstra as the graph size increases"
    )
    sizes = [25, 50, 100, 150, 200, 250]
    iterations = 3
    runs_per_size = 5

    execution_times = []
    for size in sizes:
        times_for_size = []
        for run in range(runs_per_size):
            g = Graph()
            m = g.generate_random_graph(size, size)

            source = m[size // 2][size // 2]
            dest = m[0][0]

            def dijkstra_wrapper():
                return g.dijkstra(source, dest, False)

            execution_time = timeit(dijkstra_wrapper, number=iterations)
            avg_time = execution_time / iterations
            times_for_size.append(avg_time)

            _, length = dijkstra_wrapper()
            logger.info(
                f"Graph size: {size}x{size}, Run {run + 1}, Path length: {length}"
            )

        avg_time_for_size = sum(times_for_size) / len(times_for_size)
        execution_times.append(avg_time_for_size)
        logger.info(
            f"Size {size}x{size} - Average time: {avg_time_for_size:.6f} seconds"
        )

    plot_runtime_growth(
        sizes=sizes,
        execution_times=execution_times,
        algorithm_name="Dijkstra's Algorithm (Binary Heap APQ)",
    )
    logger.info("Q3 plot saved as 'dijkstra_runtime.png'")
    return sizes, execution_times


def run_q4():
    logger.info("Running Q4: Comparing early-stop vs all-nodes Dijkstra versions")
    grid_size = 500
    center = grid_size // 2

    distances = [0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250]
    early_stop_times = []
    all_nodes_times = []
    path_lengths = []

    g = Graph()
    m = g.generate_random_graph(grid_size, grid_size)
    source = m[center][center]

    for d in distances:
        dest_row = center - d if center - d >= 0 else 0
        dest_col = center - d if center - d >= 0 else 0
        destination = m[dest_row][dest_col]

        iterations = 3

        def early_stop_wrapper():
            return g.dijkstra(source, destination, False, early_stop=True)

        def all_nodes_wrapper():
            return g.dijkstra(source, destination, False, early_stop=False)

        early_stop_time = timeit(early_stop_wrapper, number=iterations)
        early_stop_avg = early_stop_time / iterations
        early_stop_times.append(early_stop_avg)

        all_nodes_time = timeit(all_nodes_wrapper, number=iterations)
        all_nodes_avg = all_nodes_time / iterations
        all_nodes_times.append(all_nodes_avg)

        path, length = early_stop_wrapper()
        path_lengths.append(len(path))

        logger.info(f"Distance from center: {d} cells")
        logger.info(f"Path length: {len(path)} nodes, Distance: {length}")
        logger.info(
            f"Early stop time: {early_stop_avg:.6f}s, All nodes time: {all_nodes_avg:.6f}s"
        )
        logger.info(f"Speedup: {all_nodes_avg / early_stop_avg:.2f}x")

    plot_dijkstra_comparison(
        distances=distances,
        early_stop_times=early_stop_times,
        all_nodes_times=all_nodes_times,
    )
    logger.info("Q4 plot saved as 'dijkstra_comparison.png'")
    return distances, early_stop_times, all_nodes_times, path_lengths


def run_q5():
    logger.info("Running Q5: Comparing Binary Heap APQ vs Unsorted List APQ")
    sizes = [10, 20, 30, 40, 50, 75, 100]
    binary_heap_times = []
    unsorted_list_times = []

    for size in sizes:
        binary_times_for_size = []
        unsorted_times_for_size = []

        for run in range(3):  # Run multiple instances for averaging
            g = Graph()
            m = g.generate_random_graph(size, size)

            source = m[size // 2][size // 2]
            dest = m[0][0]

            def binary_heap_wrapper():
                return g.dijkstra(source, dest, False)

            def unsorted_list_wrapper():
                return g.dijkstra_list_apq(source, dest, False)

            iterations = 3

            binary_time = timeit(binary_heap_wrapper, number=iterations)
            binary_avg = binary_time / iterations
            binary_times_for_size.append(binary_avg)

            unsorted_time = timeit(unsorted_list_wrapper, number=iterations)
            unsorted_avg = unsorted_time / iterations
            unsorted_times_for_size.append(unsorted_avg)

            logger.info(f"Size {size}x{size}, Run {run + 1}:")
            logger.info(f"  Binary: {binary_avg:.6f}s, Unsorted: {unsorted_avg:.6f}s")

        avg_binary = sum(binary_times_for_size) / len(binary_times_for_size)
        avg_unsorted = sum(unsorted_times_for_size) / len(unsorted_times_for_size)

        binary_heap_times.append(avg_binary)
        unsorted_list_times.append(avg_unsorted)

        logger.info(f"Size {size}x{size} AVERAGE:")
        logger.info(f"  Binary Heap APQ: {avg_binary:.6f}s")
        logger.info(f"  Unsorted List APQ: {avg_unsorted:.6f}s")
        logger.info(f"  Ratio: {avg_unsorted / avg_binary:.2f}x")

    plot_apq_comparison(
        sizes=sizes,
        binary_heap_times=binary_heap_times,
        unsorted_list_times=unsorted_list_times,
    )
    logger.info("Q5 plot saved as 'APQ_comparison.png'")
    return sizes, binary_heap_times, unsorted_list_times


def run_q6():
    logger.info(
        "Running Q6: Comparing standard Dijkstra with simplified priority queue"
    )
    sizes = [10, 30, 50, 70, 90, 110, 130, 150]

    standard_times = []
    simple_pq_times = []

    for size in sizes:
        standard_times_for_size = []
        simple_times_for_size = []

        for run in range(3):  # Run multiple instances for averaging
            g = Graph()
            m = g.generate_random_graph(size, size)

            source = m[size // 2][size // 2]
            dest = m[0][0]

            def standard_wrapper():
                return g.dijkstra(source, dest, False)

            def simple_pq_wrapper():
                return g.dijkstra_simple_non_adaptable_pq(source, dest, False)

            iterations = 3

            standard_time = timeit(standard_wrapper, number=iterations)
            standard_avg = standard_time / iterations
            standard_times_for_size.append(standard_avg)

            simple_time = timeit(simple_pq_wrapper, number=iterations)
            simple_avg = simple_time / iterations
            simple_times_for_size.append(simple_avg)

            logger.info(f"Size {size}x{size}, Run {run + 1}:")
            logger.info(f"  Standard: {standard_avg:.6f}s, Simple: {simple_avg:.6f}s")

        avg_standard = sum(standard_times_for_size) / len(standard_times_for_size)
        avg_simple = sum(simple_times_for_size) / len(simple_times_for_size)

        standard_times.append(avg_standard)
        simple_pq_times.append(avg_simple)

        logger.info(f"Size {size}x{size} AVERAGE:")
        logger.info(f"  Standard Dijkstra: {avg_standard:.6f}s")
        logger.info(f"  Simple PQ Dijkstra: {avg_simple:.6f}s")
        logger.info(f"  Ratio: {avg_standard / avg_simple:.2f}x")

    plot_algorithms_comparison(
        sizes=sizes, standard_times=standard_times, simple_pq_times=simple_pq_times
    )
    logger.info("Q6 plot saved as 'algorithm_comparison.png'")
    return sizes, standard_times, simple_pq_times


def run_combined_comparison():
    logger.info("Running combined comparison of all PQ implementations")
    sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    binary_heap_times = []
    unsorted_list_times = []
    simple_pq_times = []

    for size in sizes:
        binary_times = []
        unsorted_times = []
        simple_times = []

        for _ in range(2):
            g = Graph()
            m = g.generate_random_graph(size, size)

            source = m[size // 2][size // 2]
            dest = m[0][0]

            def binary_heap_wrapper():
                return g.dijkstra(source, dest, False)

            def unsorted_list_wrapper():
                return g.dijkstra_list_apq(source, dest, False)

            def simple_pq_wrapper():
                return g.dijkstra_simple_non_adaptable_pq(source, dest, False)

            iterations = 2

            binary_time = timeit(binary_heap_wrapper, number=iterations)
            binary_avg = binary_time / iterations
            binary_times.append(binary_avg)

            unsorted_time = timeit(unsorted_list_wrapper, number=iterations)
            unsorted_avg = unsorted_time / iterations
            unsorted_times.append(unsorted_avg)

            simple_time = timeit(simple_pq_wrapper, number=iterations)
            simple_avg = simple_time / iterations
            simple_times.append(simple_avg)

        avg_binary = sum(binary_times) / len(binary_times)
        avg_unsorted = sum(unsorted_times) / len(unsorted_times)
        avg_simple = sum(simple_times) / len(simple_times)

        binary_heap_times.append(avg_binary)
        unsorted_list_times.append(avg_unsorted)
        simple_pq_times.append(avg_simple)

        logger.info(f"Size {size}x{size}:")
        logger.info(f"  Binary Heap: {avg_binary:.6f}s")
        logger.info(f"  Unsorted List: {avg_unsorted:.6f}s")
        logger.info(f"  Simple PQ: {avg_simple:.6f}s")

    plot_multiple_apq_comparison(
        sizes=sizes,
        binary_heap_times=binary_heap_times,
        unsorted_list_times=unsorted_list_times,
        simple_pq_times=simple_pq_times,
    )
    logger.info("Combined comparison plot saved as 'APQ_10_sizes.png'")
    return sizes, binary_heap_times, unsorted_list_times, simple_pq_times


def run_all():
    run_q3()
    run_q4()
    run_q5()
    run_q6()
    run_combined_comparison()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "q3":
            run_q3()
        elif sys.argv[1] == "q4":
            run_q4()
        elif sys.argv[1] == "q5":
            run_q5()
        elif sys.argv[1] == "q6":
            run_q6()
        elif sys.argv[1] == "combined":
            run_combined_comparison()
        elif sys.argv[1] == "all":
            run_all()
        else:
            print(f"Unknown argument: {sys.argv[1]}")
            print("Usage: python3 main.py [q3|q4|q5|q6|combined|all]")
    else:
        print("Running all evaluations...")
        run_all()
        print("All evaluations completed.")
