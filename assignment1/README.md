# Data Structures and Algorithms II - Assignment 1

This project evaluates different variants of Dijkstra's algorithm for finding
the shortest path in undirected weighted graphs.

Report doc: [REPORT](REPORT.md)

## Requirements

The code requires Python 3.9+ and the following packages:

- matplotlib
- numpy

You can install these packages using:

```bash
pip install -r requirements.txt
```

## Project Structure

- `xcollections/` - Contains implementations of:
  - `pq.py` - Priority Queue implementations (Adaptable - Binary Heap,
    Adaptable - Unsorted List, Non-adaptable - Simple PQ heap impl)
  - `graph.py` - Graph implementation and Dijkstra's algorithm variants
- `prettyplots/` - Plotting utilities
- `dijkstra_implementation_tests/` - Tests for the implemented Dijkstra's
  algorithm
- `main.py` - Benchmarking and evaluation code

### Run Tests

```bash
make test       # run all tests
make test1      # test on simplegraph1
make test2      # test on simplegraph2
```

### Run Evaluations

```bash
make q3         # run Q3: runtime evaluation as graph size increases
make q4         # run Q4: early-stop vs all-nodes comparison
make q5         # run Q5: binary heap apq vs unsorted list apq comparison
make q6         # run Q6: standard vs simplified priority queue comparison
make all_evaluations  # run all evaluations
```

### Clean

```bash
make clean #removes the generated images of plots
```
