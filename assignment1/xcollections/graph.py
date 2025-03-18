import uuid
from typing import cast
from typing import Any
from xcollections.pq import AdaptablePQ, AdaptablePQUnsortedList, SimplePQ
import random


class Vertex:
    def __init__(self, label: Any, id: uuid.UUID | str | None = None) -> None:
        self.id = id if id is not None else uuid.uuid4()
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
    def __init__(self) -> None:
        self.graph: dict[Vertex, dict[Vertex, Edge]] = {}
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
        # assuming edges are undirected
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

    BreadthFirstSearchResult = tuple[dict[Vertex, tuple[Edge, int] | None], int]

    def breadthfirstsearch(self, v: Vertex) -> BreadthFirstSearchResult:
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

    def dijkstra_simple_non_adaptable_pq(
        self, src: Vertex, dest: Vertex, print_result=False, early_stop=True
    ):
        dist = {v: float("inf") for v in self.graph}
        dist[src] = 0
        prev = {v: None for v in self.graph}  # used to reconstruct the path

        pq = SimplePQ()

        for v in self.graph:
            priority = 0 if v == src else float("inf")
            dist[v] = priority
            prev[v] = None
            pq.add(v, priority)

        while len(pq) > 0:
            u, u_dist = pq.pop()

            if early_stop and u == dest:
                break

            for e in self.get_edges(u):
                v = e.opposite(u)
                weight = e.element()
                alt_dist = u_dist + weight

                if alt_dist < dist[v]:
                    dist[v] = alt_dist
                    prev[v] = u
                    # instead of updating the priority just add a new item. The smaller priority will always be first
                    pq.add(v, alt_dist)

        path = []
        current = dest

        if prev[dest] is None and dest != src:
            return [], float("inf")

        while current is not None:
            path.append(current)
            current = prev[current]

        path.reverse()

        if print_result:  # TODO: Maybe move this out ?
            print("\n=== DIJKSTRA RESULT ===")
            print(
                f"Shortest path from {src.element()} to {dest.element()}: {' -> '.join([v.element() for v in path])}"
            )
            print(f"Total distance: {dist[dest]}")

            print("\nDetailed path:")
            for i in range(len(path) - 1):
                edge = self.get_edge(path[i], path[i + 1])
                print(
                    f"{path[i].element()} to {path[i + 1].element()} (weight: {edge.element()})"
                )
            print("=== END RESULT ===\n")

        return path, dist[dest]

    def dijkstra_list_apq(
        self, src: Vertex, dest: Vertex, print_result=False, early_stop=True
    ):
        dist = {v: float("inf") for v in self.graph}
        dist[src] = 0
        prev = {v: None for v in self.graph}  # used to reconstruct the path

        pq = AdaptablePQUnsortedList()

        for v in self.graph:
            priority = 0 if v == src else float("inf")
            dist[v] = priority
            prev[v] = None
            pq.add(v, priority)

        while len(pq) > 0:
            u, u_dist = pq.pop()

            if early_stop and u == dest:
                break

            for e in self.get_edges(u):
                v = e.opposite(u)
                weight = e.element()
                alt_dist = u_dist + weight

                if alt_dist < dist[v]:
                    dist[v] = alt_dist
                    prev[v] = u
                    pq.update_priority(v, alt_dist)

        path = []
        current = dest

        if prev[dest] is None and dest != src:
            return [], float("inf")

        while current is not None:
            path.append(current)
            current = prev[current]

        path.reverse()

        if print_result:  # TODO: Maybe move this out ?
            print("\n=== DIJKSTRA RESULT ===")
            print(
                f"Shortest path from {src.element()} to {dest.element()}: {' -> '.join([v.element() for v in path])}"
            )
            print(f"Total distance: {dist[dest]}")

            print("\nDetailed path:")
            for i in range(len(path) - 1):
                edge = self.get_edge(path[i], path[i + 1])
                print(
                    f"{path[i].element()} to {path[i + 1].element()} (weight: {edge.element()})"
                )
            print("=== END RESULT ===\n")

        return path, dist[dest]

    def dijkstra(
        self, src: Vertex, dest: Vertex, print_result=False, early_stop=True
    ) -> tuple[list[Vertex], float]:
        dist = {}
        prev = {}
        pq = AdaptablePQ()

        for v in self.graph:
            priority = 0 if v == src else float("inf")
            dist[v] = priority
            prev[v] = None
            pq.add(v, priority)

        while len(pq) > 0:
            u, u_dist = pq.pop()

            if early_stop and u == dest:
                break

            for e in self.get_edges(u):
                v = e.opposite(u)
                weight = e.element()
                alt_dist = u_dist + weight

                if alt_dist < dist[v]:
                    dist[v] = alt_dist
                    prev[v] = u
                    pq.update_priority(v, alt_dist)

        path = []
        current = dest

        if prev[dest] is None and dest != src:
            return [], float("inf")

        while current is not None:
            path.append(current)
            current = prev[current]

        path.reverse()

        if print_result:  # TODO: Maybe move this out ?
            print("\n=== DIJKSTRA RESULT ===")
            print(
                f"Shortest path from {src.element()} to {dest.element()}: {' -> '.join([v.element() for v in path])}"
            )
            print(f"Total distance: {dist[dest]}")

            print("\nDetailed path:")
            for i in range(len(path) - 1):
                edge = self.get_edge(path[i], path[i + 1])
                print(
                    f"{path[i].element()} to {path[i + 1].element()} (weight: {edge.element()})"
                )
            print("=== END RESULT ===\n")

        return path, dist[dest]

    def generate_random_graph(self, n: int, m: int) -> list[list[Vertex]]:
        node_matrix: list[list[Vertex | None]] = [
            [None for _ in range(m)] for _ in range(n)
        ]

        # create vertices
        for i in range(n):
            for j in range(m):
                v = Vertex(f"v{i}_{j}")
                node_matrix[i][j] = v
                # Add vertex by insantance. Might move it to a method ?
                self.graph[v] = {}

        # create the edges
        for i in range(n):
            for j in range(m):
                if i + 1 < n:
                    v1 = node_matrix[i][j]
                    v2 = node_matrix[i + 1][j]
                    if v1 is not None and v2 is not None:
                        self.add_edge(
                            v1,
                            v2,
                            random.randint(1, max(n, m) // 2),
                        )
                if j + 1 < m:
                    v1 = node_matrix[i][j]
                    v2 = node_matrix[i][j + 1]
                    if v1 is not None and v2 is not None:
                        self.add_edge(
                            v1,
                            v2,
                            random.randint(1, max(n, m) // 2),
                        )
        # done for the sake of the lsp
        node_matrix_casted = cast(list[list[Vertex]], node_matrix)
        return node_matrix_casted
