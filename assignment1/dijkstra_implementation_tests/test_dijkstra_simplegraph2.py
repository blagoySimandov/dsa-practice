from xcollections.graph import Graph


def test_dijkstra_large():
    g = Graph()

    nodes = {}
    for i in range(1, 29):
        nodes[i] = g.add_vertex(f"Node {i}")

    g.add_edge(nodes[1], nodes[2], 2)
    g.add_edge(nodes[1], nodes[4], 8)
    g.add_edge(nodes[2], nodes[5], 7)
    g.add_edge(nodes[2], nodes[6], 5)
    g.add_edge(nodes[3], nodes[6], 4)
    g.add_edge(nodes[3], nodes[10], 6)
    g.add_edge(nodes[3], nodes[11], 2)
    g.add_edge(nodes[4], nodes[7], 5)
    g.add_edge(nodes[4], nodes[7], 5)
    g.add_edge(nodes[5], nodes[8], 3)
    g.add_edge(nodes[5], nodes[9], 1)
    g.add_edge(nodes[6], nodes[8], 3)
    g.add_edge(nodes[7], nodes[12], 2)
    g.add_edge(nodes[8], nodes[9], 5)
    g.add_edge(nodes[9], nodes[15], 4)
    g.add_edge(nodes[10], nodes[14], 1)
    g.add_edge(nodes[11], nodes[14], 4)
    g.add_edge(nodes[11], nodes[16], 3)
    g.add_edge(nodes[12], nodes[15], 6)
    g.add_edge(nodes[13], nodes[14], 7)
    g.add_edge(nodes[13], nodes[15], 6)
    g.add_edge(nodes[14], nodes[21], 5)
    g.add_edge(nodes[15], nodes[17], 2)
    g.add_edge(nodes[15], nodes[18], 5)
    g.add_edge(nodes[15], nodes[20], 3)
    g.add_edge(nodes[16], nodes[19], 4)
    g.add_edge(nodes[17], nodes[22], 6)
    g.add_edge(nodes[18], nodes[21], 8)
    g.add_edge(nodes[19], nodes[23], 6)
    g.add_edge(nodes[20], nodes[24], 1)
    g.add_edge(nodes[21], nodes[25], 8)
    g.add_edge(nodes[22], nodes[24], 5)
    g.add_edge(nodes[22], nodes[26], 7)
    g.add_edge(nodes[23], nodes[28], 5)
    g.add_edge(nodes[24], nodes[26], 6)
    g.add_edge(nodes[24], nodes[27], 10)
    g.add_edge(nodes[25], nodes[27], 5)
    g.add_edge(nodes[25], nodes[28], 4)
    g.add_edge(nodes[26], nodes[27], 3)
    g.add_edge(nodes[27], nodes[28], 3)

    g.dijkstra(nodes[14], nodes[5], print_result=True)


if __name__ == "__main__":
    test_dijkstra_large()
