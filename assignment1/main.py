from xcollections.graph import Graph
import pprint

g = Graph()
m = g.generate_random_graph(4, 4)
pprint.pprint(str(g))
