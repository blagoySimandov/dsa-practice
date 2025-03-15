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
