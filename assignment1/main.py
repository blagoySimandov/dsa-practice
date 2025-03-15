from xcollections.graph import Graph

g = Graph()
m = g.generate_random_graph(4, 4)
g.dijkstra(m[0][0], m[3][3], True)
