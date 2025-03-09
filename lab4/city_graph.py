from main import Graph


def create_city_graph():
    g = Graph()

    # Create city vertices
    nyc = g.add_vertex("New York")
    bos = g.add_vertex("Boston")
    phi = g.add_vertex("Philadelphia")
    dc = g.add_vertex("Washington DC")
    chi = g.add_vertex("Chicago")

    # Add roads (edges) with distances in miles
    g.add_edge(nyc, bos, "215 miles")
    g.add_edge(nyc, phi, "95 miles")
    g.add_edge(phi, dc, "140 miles")
    g.add_edge(nyc, dc, "225 miles")
    g.add_edge(nyc, chi, "790 miles")
    g.add_edge(bos, chi, "980 miles")

    return g


city_graph = create_city_graph()
# Print graph information
print(f"Number of cities: {city_graph.num_vertices()}")
print(f"Number of roads: {city_graph.num_edges()}")
print("\nCities in the graph:")
for city in city_graph.vertices():
    print(f"- {city.element()}")

print("\nRoads in the graph:")
for road in city_graph.edges():
    print(f"- {road} ({road.element()})")

print("\nDetailed graph representation:")
print(city_graph)
