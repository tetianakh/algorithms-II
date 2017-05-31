

class Graph:
    def __init__(self, V):
        self._V = V
        self._adj = [set() for _ in range(V)]

    def add_edge(self, v, w):
        self._adj[v].add(w)
        self._adj[w].add(v)

    def adjacent(self, v):
        return iter(self._adj[v])

    @property
    def num_vertices(self):
        return self._V


def test_added_edge_is_adjacent():
    graph = Graph(2)
    graph.add_edge(0, 1)
    assert list(graph.adjacent(0)) == [1]
    assert list(graph.adjacent(1)) == [0]
