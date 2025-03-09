from city_graph import create_city_network

graph, new_york = create_city_network()
# print(graph.breadthfirstsearch(new_york))

print(graph.breadthfirstsearch(new_york)[0])
print("Max level")
print(graph.breadthfirstsearch(new_york)[1])
levels = []
for v in graph:
    levels.append((v, graph.breadthfirstsearch(v)[1]))

min = levels[0]
for l in levels:
    if l[1] < min[1]:
        min = l


print(min)
