import uuid


class Vertex:
    def __init__(self, label: str, id: uuid.UUID | str = uuid.uuid4()) -> None:
        self.id = id
        self.label = label

    def element(self):
        return self.label

    def __str__(self) -> str:
        return f"Vertex: {self.label}"

    def __repr__(self) -> str:
        return self.__str__()


class Edge:
    def __init__(
        self, u: Vertex, v: Vertex, label: str, id: uuid.UUID | str = uuid.uuid4()
    ) -> None:
        self.id = id
        self.u = u
        self.v = v
        self.label = label

    def element(self):
        return self.label

    def opposite(self, c: Vertex):
        return self.v if c == self.u else self.u

    def __str__(self) -> str:
        return f"({self.u.element()} - {self.v.element()})"

    def __repr__(self) -> str:
        return self.__str__()


class Graph:
    graph: dict[Vertex, dict[Vertex, Edge]] = {}

    def __init__(self) -> None:
        pass

    def vertices(self) -> list[Vertex]:
        return list(self.graph.keys())

    def edges(self) -> list[Edge]:
        edges = []
        for vertex in self.graph:
            for edge in self.graph[vertex].values():
                edges.append(edge)
        return edges

    def num_vertices(self) -> int:
        return len(self.graph)

    def num_edges(self) -> int:
        return len(self.edges())

    def get_edge(self, v1: Vertex, v2: Vertex) -> Edge:
        return self.graph[v1][v2]

    def degree(self, v: Vertex) -> int:
        return len(self.graph[v])

    def get_edges(self, x: Vertex):
        return self.graph[x]

    def add_vertex(self, label: str) -> Vertex:
        v = Vertex(label)
        self.graph[v] = {}
        return v

    def add_edge(self, u: Vertex, v: Vertex, label: str) -> Edge:
        e = Edge(u, v, label)
        self.graph[u][v] = e
        self.graph[v][u] = e
        return e

    def __str__(self) -> str:
        result = "Graph:\n"
        for v in self.vertices():
            result += f"  {v} connected to: "
            connections = []
            for neighbor in self.graph[v]:
                edge = self.graph[v][neighbor]
                connections.append(f"{neighbor} (via {edge.element()})")
            result += ", ".join(connections) + "\n"
        return result
