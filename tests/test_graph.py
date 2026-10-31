import unittest

from course_registration_sorting.graph import CycleError, Graph, is_topological_order


def diamond() -> Graph:
    # a -> b -> d, a -> c -> d, plus an isolated vertex e
    return Graph({"a": ["b", "c"], "b": ["d"], "c": ["d"], "d": [], "e": []})


class GraphTest(unittest.TestCase):
    def test_add_edge_adds_missing_vertices(self):
        g = Graph()
        g.add_edge("x", "y")
        self.assertEqual(g.vertices(), ["x", "y"])
        self.assertEqual(g.edges(), [("x", "y")])

    def test_empty_graph(self):
        self.assertEqual(Graph().dfs(), ({}, {}))
        self.assertEqual(Graph().topological_sort(), [])

    def test_single_vertex(self):
        g = Graph({"a": []})
        self.assertEqual(g.dfs(), ({"a": 1}, {"a": 2}))
        self.assertEqual(g.topological_sort(), ["a"])

    def test_chain_listed_backwards(self):
        # DFS starts at c, so the result cannot just be the insertion order
        g = Graph({"c": [], "b": ["c"], "a": ["b"]})
        self.assertEqual(g.topological_sort(), ["a", "b", "c"])

    def test_pre_post_numbers_by_hand(self):
        # explore(a): a pre 1, b pre 2, d pre 3, d post 4, b post 5, c pre 6, c post 7, a post 8; then e 9/10
        pre, post = diamond().dfs()
        self.assertEqual(pre, {"a": 1, "b": 2, "d": 3, "c": 6, "e": 9})
        self.assertEqual(post, {"d": 4, "b": 5, "c": 7, "a": 8, "e": 10})

    def test_order_is_decreasing_post(self):
        self.assertEqual(diamond().topological_sort(), ["e", "a", "c", "b", "d"])

    def test_every_edge_goes_from_higher_to_lower_post(self):
        g = diamond()
        _, post = g.dfs()
        for v, u in g.edges():
            self.assertGreater(post[v], post[u], f"{v} -> {u}")

    def test_first_vertex_is_a_source(self):
        g = Graph({"x": ["y"], "y": ["z"], "z": [], "w": ["y"]})
        first = g.topological_sort()[0]
        self.assertNotIn(first, [u for _, u in g.edges()])

    def test_disconnected_parts(self):
        g = Graph({"a": ["b"], "b": [], "c": ["d"], "d": [], "e": []})
        order = g.topological_sort()
        self.assertTrue(is_topological_order(g.vertices(), g.edges(), order))

    def test_cycle_raises(self):
        g = Graph({"a": ["b"], "b": ["c"], "c": ["a"]})
        with self.assertRaises(CycleError) as caught:
            g.topological_sort()
        self.assertEqual(caught.exception.edge, ("c", "a"))

    def test_self_loop_raises(self):
        with self.assertRaises(CycleError):
            Graph({"a": ["a"]}).topological_sort()


class IsTopologicalOrderTest(unittest.TestCase):
    vertices = ["a", "b", "c"]
    edges = [("a", "b"), ("b", "c")]

    def test_valid(self):
        self.assertTrue(is_topological_order(self.vertices, self.edges, ["a", "b", "c"]))

    def test_edge_out_of_order(self):
        self.assertFalse(is_topological_order(self.vertices, self.edges, ["b", "a", "c"]))

    def test_missing_vertex(self):
        self.assertFalse(is_topological_order(self.vertices, self.edges, ["a", "b"]))

    def test_repeated_vertex(self):
        self.assertFalse(is_topological_order(self.vertices, self.edges, ["a", "b", "b", "c"]))


if __name__ == "__main__":
    unittest.main()
