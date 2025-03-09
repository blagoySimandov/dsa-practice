import uuid
from typing import Any


class Vertex:
    def __init__(self, label: Any, id: uuid.UUID | str = uuid.uuid4()) -> None:
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
        self, u: Vertex, v: Vertex, label: Any, id: uuid.UUID | str = uuid.uuid4()
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

    def __iter__(self):
        return iter(self.graph)

    def num_vertices(self) -> int:
        return len(self.graph)

    def num_edges(self) -> int:
        return len(self.edges())

    def get_edge(self, v1: Vertex, v2: Vertex) -> Edge:
        return self.graph[v1][v2]

    def degree(self, v: Vertex) -> int:
        return len(self.graph[v])

    def get_edges(self, x: Vertex):
        return list(self.graph[x].values())

    def add_vertex(self, label: str) -> Vertex:
        v = Vertex(label)
        self.graph[v] = {}
        return v

    def add_edge(self, u: Vertex, v: Vertex, element: Any) -> Edge:
        e = Edge(u, v, element)
        self.graph[u][v] = e
        self.graph[v][u] = e
        return e

    BreathFirstSearchResult = tuple[dict[Vertex, tuple[Edge, int] | None], int]

    def breadthfirstsearch(self, v: Vertex) -> BreathFirstSearchResult:
        marked: dict[Vertex, tuple[Edge, int] | None] = {v: None}
        queue = [v]  # TODO: fix this to use a proper q
        level = 0
        max_level = 0

        while queue:
            level_size = len(queue)  # Process all nodes at current level
            level += 1

            for _ in range(level_size):
                current = queue.pop(0)
                for e in self.get_edges(current):
                    w = e.opposite(current)
                    if w not in marked:
                        marked[w] = (e, level)
                        max_level = (
                            level  # Update max level when we find a node at a new level
                        )
                        queue.append(w)

        return (marked, max_level)

    def depthfirstsearch(self, v: Vertex) -> dict[Vertex, Edge | None]:
        marked: dict[Vertex, Edge | None] = {v: None}
        self._depthfirstsearch(v, marked)
        return marked

    def _depthfirstsearch(self, v: Vertex, marked: dict[Vertex, None | Edge]):
        for e in self.get_edges(v):
            w = e.opposite(v)
            if w not in marked:
                marked[w] = e
                self._depthfirstsearch(w, marked)

    # str repestentation of the graph is taken from stackoverflow
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
