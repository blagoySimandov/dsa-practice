from city_graph import create_city_network

graph, new_york = create_city_network()
# print(graph.breadthfirstsearch(new_york))
print(graph.depthfirstsearch(new_york))
