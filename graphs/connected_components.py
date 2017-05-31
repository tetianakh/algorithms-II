from graph import Graph
import pytest


class ConnectedComponents:
    def __init__(self, graph):
        self._components = [None for _ in range(graph.num_vertices)]
        self._visited = set()
        self._find_components(graph)

    def _find_components(self, graph):
        for vertex in graph:
            if self._components[vertex] is None:
                self._walk(graph, vertex)

    def _walk(self, graph, start):
        stack = list()
        stack.append(start)
        self._visited.add(start)
        self._components[start] = start
        while stack:
            vertex = stack.pop()
            for adjacent in graph.adjacent(vertex):
                if adjacent in self._visited:
                    continue
                stack.append(adjacent)
                self._visited.add(adjacent)
                self._components[adjacent] = start

    def component_id(self, v):
        return self._components[v]

    def are_connected(self, v, w):
        return (self._components[v] == self._components[w])

    @property
    def num_components(self):
        return len(set(self._components))


class TestSingleComponent:
    @pytest.fixture
    def components(self):
        graph = Graph(2)
        graph.add_edge(0, 1)
        return ConnectedComponents(graph)

    def test_has_one_component(self, components):
        assert components.num_components == 1

    def test_component_id(self, components):
        assert components.component_id(0) == 0
        assert components.component_id(1) == 0

    def test_vertices_in_component_are_connected(self, components):
        assert components.are_connected(0, 1) is True


class TestThreeComponents:
    @pytest.fixture
    def components(self):
        graph = Graph(6)
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(3, 4)
        return ConnectedComponents(graph)

    def test_has_three_components(self, components):
        assert components.num_components == 3

    @pytest.mark.parametrize(('vertex', 'id'), [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 3),
        (4, 3),
        (5, 5),
    ])
    def test_component_id(self, components, vertex, id):
        assert components.component_id(vertex) == id

    @pytest.mark.parametrize(('v', 'w'), [
        (1, 0),
        (2, 0),
        (1, 2),
        (3, 4),
    ])
    def test_vertices_in_component_are_connected(self, components, v, w):
        assert components.are_connected(v, w) is True

    @pytest.mark.parametrize(('v', 'w'), [
        (0, 3),
        (1, 3),
        (2, 3),
        (0, 4),
        (1, 4),
        (2, 4),
        (0, 5),
        (1, 5),
        (2, 5),
        (3, 5),
        (4, 5),
    ])
    def test_vertices_from_different_components_are_not_connected(self, components, v, w):   # noqa
        assert components.are_connected(v, w) is False
