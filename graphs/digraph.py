

class Digraph:
    def __init__(self, V):
        self._adj = [set() for _ in range(V)]

    def add_edge(self, v, w):
        self._adj[v].add(w)

    def adjacent(self, v):
        return iter(self._adj[v])

    @property
    def num_vertices(self):
        return len(self._adj)


def test_added_edge_is_adjacent_one_way():
    digraph = Digraph(2)
    digraph.add_edge(0, 1)
    assert list(digraph.adjacent(0)) == [1]
    assert list(digraph.adjacent(1)) == []


def test_number_of_vertices():
    digraph = Digraph(2)
    digraph.add_edge(0, 1)
    assert digraph.num_vertices == 2
