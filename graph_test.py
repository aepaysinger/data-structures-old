import pytest

from graph import Graph


def test_add_node():
    graph = Graph()
    graph.add_node(4)

    assert graph.storage == {4: []}


def test_nodes():
    graph = Graph()
    graph.add_node(4)
    graph.add_node(7)
    graph.add_node(9)

    assert graph.nodes() == [4, 7, 9]


def test_add_edge():
    graph = Graph()
    graph.add_edge(4, 16)
    graph.add_edge(4, 8)
    graph.add_edge(9, 81)

    assert graph.storage == {4: [16, 8], 9: [81], 16: [4], 8: [4], 81: [9]}


def test_edges():
    graph = Graph()
    graph.add_edge(4, 16)
    graph.add_edge(4, 8)
    graph.add_edge(9, 81)

    assert graph.edges() == [[16, 8], [4], [4], [81], [9]]


def test_delete_node():
    graph = Graph()
    graph.add_edge(4, 16)
    graph.add_edge(4, 8)
    graph.add_edge(9, 81)
    graph.add_edge(7, 49)
    graph.del_node(4)

    assert graph.storage == {
        16: [],
        8: [],
        9: [81],
        81: [9],
        7: [49],
        49: [7],
    }

    with pytest.raises(ValueError) as exc_info:
        graph.del_node(10)
    assert exc_info.value.args[0] == "Node does not exist"


def test_has_node():
    graph = Graph()
    graph.add_edge(4, 16)
    graph.add_edge(4, 8)
    graph.add_edge(9, 81)

    assert graph.has_node(4) == True
    assert graph.has_node(7) == False


def test_delete_edge():
    graph = Graph()
    graph.add_edge(4, 16)
    graph.add_edge(4, 8)
    graph.add_edge(9, 81)
    graph.add_edge(7, 49)

    assert graph.storage == {
        4: [16, 8],
        16: [4],
        8: [4],
        9: [81],
        81: [9],
        7: [49],
        49: [7],
    }

    graph.del_edge(4, 16)

    assert graph.storage == {
        4: [8],
        16: [],
        8: [4],
        9: [81],
        81: [9],
        7: [49],
        49: [7],
    }

    with pytest.raises(ValueError) as exc_info:
        graph.del_edge(5, 81)
    assert exc_info.value.args[0] == "Edge does not exist"

    with pytest.raises(ValueError) as exc_info:
        graph.del_edge(4, 12)
    assert exc_info.value.args[0] == "Edge does not exist"


def test_neighbors():
    graph = Graph()
    graph.add_edge(4, 16)
    graph.add_edge(4, 8)
    graph.add_edge(9, 81)
    graph.add_edge(7, 49)

    assert graph.neighbors(4) == [16, 8]

    with pytest.raises(ValueError) as exc_info:
        graph.neighbors(3)
    assert exc_info.value.args[0] == "Value does not exist"


def test_adjecent():
    graph = Graph()
    graph.add_edge(4, 16)
    graph.add_edge(4, 8)
    graph.add_edge(9, 81)
    graph.add_edge(7, 49)

    assert graph.adjcent(9, 81) == True

    with pytest.raises(ValueError) as exc_info:
        graph.adjcent(3, 16)
    assert exc_info.value.args[0] == "Value does not exist"

    with pytest.raises(ValueError) as exc_info:
        graph.adjcent(4, 12)
    assert exc_info.value.args[0] == "Value does not exist"


def test_depth_first_traversal():
    graph = Graph()
    graph.add_edge(4, 16)
    graph.add_edge(4, 8)
    graph.add_edge(9, 81)
    
    assert graph.depth_first_traversal(4) == [4, 16, 8, 81, 9]

    