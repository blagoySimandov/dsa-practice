from collections.graph import Graph


def test_dijkstra_custom():
    g = Graph()

    nodes = {}
    for i in range(1, 6):
        nodes[i] = g.add_vertex(f"Node {i}")

    g.add_edge(nodes[1], nodes[2], 3)

    g.add_edge(nodes[1], nodes[3], 8)

    g.add_edge(nodes[1], nodes[5], 5)

    g.add_edge(nodes[2], nodes[3], 4)

    g.add_edge(nodes[3], nodes[4], 1)

    g.add_edge(nodes[3], nodes[5], 6)

    g.add_edge(nodes[4], nodes[5], 4)

    print(g)

    print("\nShortest path from Node 1 to Node 4:")
    path, distance = g.dijkstra(nodes[1], nodes[4])

    if path:
        print(f"Distance: {distance}")
        print("Path:", " -> ".join([v.element() for v in path]))

        print("\nDetailed path:")
        for i in range(len(path) - 1):
            edge = g.get_edge(path[i], path[i + 1])
            print(
                f"{path[i].element()} to {path[i + 1].element()} (weight: {edge.element()})"
            )
    else:
        print("No path found")


if __name__ == "__main__":
    test_dijkstra_custom()

