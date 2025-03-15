from xcollections.graph import Graph
from timeit import timeit


g = Graph()
m = g.generate_random_graph(500, 500)


def dijkstra_wrapper():
    g.dijkstra(m[0][0], m[499][499], True)


execution_time = timeit(dijkstra_wrapper, number=10)
print(f"Execution time: {execution_time / 10}")
