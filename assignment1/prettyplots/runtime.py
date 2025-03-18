import matplotlib.pyplot as plt
import numpy as np


def plot_runtime_growth(
    sizes,
    execution_times,
    algorithm_name="Algorithm",
):
    fig = plt.figure(figsize=(10, 6))
    plt.plot(sizes, execution_times, "o-", linewidth=2, markersize=8)
    plt.xlabel("Input Size (n)", fontsize=12)
    plt.ylabel("Execution Time (seconds)", fontsize=12)
    plt.title(f"{algorithm_name} Runtime Growth", fontsize=14)
    plt.grid(True, linestyle="--", alpha=0.7)

    for _, (size, time) in enumerate(zip(sizes, execution_times)):
        plt.annotate(
            f"{time:.4f}s",
            (size, time),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
        )

    plt.tight_layout()
    plt.savefig("figs/dijkstra_runtime.png")
    return fig


def plot_dijkstra_comparison(
    distances,
    early_stop_times,
    all_nodes_times,
):
    fig = plt.figure(figsize=(15, 8))

    plt.subplot(2, 2, 1)
    plt.plot(distances, early_stop_times, "b-o", label="Early Stop")
    plt.plot(distances, all_nodes_times, "r-o", label="All Nodes")
    plt.xlabel("Distance from Center (cells)")
    plt.ylabel("Runtime (seconds)")
    plt.title("Runtime Comparison")
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 2, 2)
    speedups = [
        all_nodes / early for all_nodes, early in zip(all_nodes_times, early_stop_times)
    ]
    plt.plot(distances, speedups, "g-o")
    plt.xlabel("Distance from Center (cells)")
    plt.ylabel("Speedup Factor")
    plt.title("Speedup of Early Stop vs All Nodes")
    plt.axhline(y=1, color="r", linestyle="--", label="Break-even point")
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("figs/dijkstra_comparison.png")
    return fig


def plot_apq_comparison(sizes, binary_heap_times, unsorted_list_times):
    fig = plt.figure(figsize=(12, 8))

    plt.subplot(2, 1, 1)
    plt.plot(sizes, binary_heap_times, "b-o", label="Binary Heap APQ")
    plt.plot(sizes, unsorted_list_times, "r-o", label="Unsorted List APQ")
    plt.xlabel("Grid Size")
    plt.ylabel("Runtime (seconds)")
    plt.title("Runtime Comparison: Binary Heap vs Unsorted List APQ")
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 1, 2)
    ratios = [
        unsorted / binary
        for unsorted, binary in zip(unsorted_list_times, binary_heap_times)
    ]
    plt.bar(sizes, ratios, color="green", alpha=0.7)
    for i, ratio in enumerate(ratios):
        plt.text(sizes[i], ratio + 0.1, f"{ratio:.1f}x", ha="center")
    plt.axhline(y=1, color="r", linestyle="--")
    plt.xlabel("Grid Size")
    plt.ylabel("Ratio (Unsorted List / Binary Heap)")
    plt.title("Performance Ratio of APQ Implementations")
    plt.grid(True, axis="y")

    plt.tight_layout()
    plt.savefig("figs/APQ_comparison.png")
    return fig


def plot_algorithms_comparison(sizes, standard_times, simple_pq_times):
    fig = plt.figure(figsize=(12, 8))

    plt.subplot(2, 1, 1)
    plt.plot(sizes, standard_times, "b-o", label="Standard Dijkstra with APQ")
    plt.plot(sizes, simple_pq_times, "r-o", label="Simplified PQ Dijkstra")
    plt.xlabel("Grid Size")
    plt.ylabel("Runtime (seconds)")
    plt.title("Runtime Comparison: Standard vs Simplified PQ Dijkstra")
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 1, 2)
    ratios = [
        standard / simple for standard, simple in zip(standard_times, simple_pq_times)
    ]
    plt.bar(sizes, ratios, color="purple", alpha=0.7)
    for i, ratio in enumerate(ratios):
        plt.text(sizes[i], ratio + 0.1, f"{ratio:.1f}x", ha="center")
    plt.axhline(y=1, color="r", linestyle="--")
    plt.xlabel("Grid Size")
    plt.ylabel("Ratio (Standard / Simplified)")
    plt.title("Performance Ratio of Dijkstra Implementations")
    plt.grid(True, axis="y")

    plt.tight_layout()
    plt.savefig("figs/algorithm_comparison.png")
    return fig


def plot_multiple_apq_comparison(
    sizes, binary_heap_times, unsorted_list_times, simple_pq_times
):
    fig = plt.figure(figsize=(12, 10))

    plt.subplot(2, 1, 1)
    plt.plot(sizes, binary_heap_times, "b-o", label="Binary Heap APQ")
    plt.plot(sizes, unsorted_list_times, "r-o", label="Unsorted List APQ")
    plt.plot(sizes, simple_pq_times, "g-o", label="Simple PQ")
    plt.xlabel("Grid Size")
    plt.ylabel("Runtime (seconds)")
    plt.title("Runtime Comparison of Different PQ Implementations")
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 1, 2)
    bin_unsorted_ratios = [
        unsorted / binary
        for unsorted, binary in zip(unsorted_list_times, binary_heap_times)
    ]
    bin_simple_ratios = [
        simple / binary for simple, binary in zip(simple_pq_times, binary_heap_times)
    ]

    bar_width = 0.35
    index = np.arange(len(sizes))

    plt.bar(
        index - bar_width / 2,
        bin_unsorted_ratios,
        bar_width,
        color="red",
        alpha=0.7,
        label="Unsorted/Binary",
    )
    plt.bar(
        index + bar_width / 2,
        bin_simple_ratios,
        bar_width,
        color="green",
        alpha=0.7,
        label="Simple/Binary",
    )

    plt.axhline(y=1, color="black", linestyle="--")
    plt.xlabel("Grid Size")
    plt.ylabel("Ratio Compared to Binary Heap")
    plt.title("Performance Ratios")
    plt.xticks(index, sizes)
    plt.legend()
    plt.grid(True, axis="y")

    plt.tight_layout()
    plt.savefig("figs/APQ_10_sizes.png")
    return fig
