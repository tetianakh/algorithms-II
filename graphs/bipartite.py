from graph import Graph

BLACK = 'BLACK'
RED = 'RED'


def is_bipartite(graph):
    start = 0
    stack = list()
    visited = set()
    colors = [None for _ in range(graph.num_vertices)]
    stack.append(start)
    visited.add(start)
    colors[start] = BLACK
    while stack:
        v = stack.pop()
        for a in graph.adjacent(v):
            if a in visited:
                if colors[a] != opposite(colors[v]):
                    return False
                continue
            stack.append(a)
            visited.add(a)
            colors[a] = opposite(colors[v])
    return True


def opposite(color):
    return RED if color == BLACK else BLACK


def test_linear_graph_is_bipartite():
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    assert is_bipartite(g) == True

def test_triangular_graph_is_not_bipartite():
    g = Graph(3)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    assert is_bipartite(g) == False
