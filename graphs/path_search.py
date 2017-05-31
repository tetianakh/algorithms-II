from collections import deque
import pytest

from graph import Graph


class GraphPath():

    def __init__(self, graph, start=0):
        self._visited = set()
        self._edge_to = [None for _ in range(graph.num_vertices)]
        self._start = start
        self._walk(graph, start)

    def has_path_to(self, v):
        return v in self._visited

    def path_to(self, v):
        result = []
        if self._edge_to[v] is None:
            return result
        next_ = v
        while next_ != None:
            result.append(next_)
            next_ = self._edge_to[next_]
        return result[::-1]


class DFS(GraphPath):

    def _walk(self, graph, v):
        """Marks all vertices connected to v"""
        self._visited.add(v)
        for vertice in graph.adjacent(v):
            if vertice in self._visited:
                continue
            self._walk(graph, vertice)
            self._edge_to[vertice] = v


class BFS(GraphPath):

    def _walk(self, graph, start):
        queue = deque()
        queue.append(start)
        self._visited.add(start)
        while queue:
            vertex = queue.popleft()
            for a in graph.adjacent(vertex):
                if a in self._visited:
                    continue
                queue.append(a)
                self._visited.add(a)
                self._edge_to[a] = vertex


@pytest.mark.parametrize('PathSearch', [BFS, DFS])
def test_dfs_no_path(PathSearch):
    graph = Graph(2)
    path = PathSearch(graph)
    assert path.has_path_to(1) is False
    assert path.path_to(1) == []


@pytest.mark.parametrize('PathSearch', [BFS, DFS])
def test_dfs_path(PathSearch):
    graph = Graph(2)
    graph.add_edge(0, 1)
    path = PathSearch(graph)
    assert path.has_path_to(1) is True
    assert path.path_to(1) == [0, 1]
