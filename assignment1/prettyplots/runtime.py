import matplotlib.pyplot as plt


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

    plt.legend()
    plt.tight_layout()

    return fig

def plot_dijkstra_comparison(distances, early_stop_times, all_nodes_times, path_lengths):
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.plot(distances, early_stop_times, 'b-o', label='Early Stop (Original)')
    plt.plot(distances, all_nodes_times, 'r-o', label='All Nodes')
    plt.xlabel('Distance from Center (cells)')
    plt.ylabel('Runtime (seconds)')
    plt.title('Runtime Comparison of Dijkstra Implementations')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(1, 2, 2)
    speedups = [all_nodes / early for all_nodes, early in zip(all_nodes_times, early_stop_times)]
    plt.plot(distances, speedups, 'g-o')
    plt.xlabel('Distance from Center (cells)')
    plt.ylabel('Speedup Factor')
    plt.title('Speedup of Early Stop vs All Nodes')
    plt.axhline(y=1, color='r', linestyle='--', label='Break-even point')
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('dijkstra_comparison.png')
