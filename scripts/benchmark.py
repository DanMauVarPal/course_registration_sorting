"""Time topological_sort on random DAGs of growing size; flat ns/(V+E) means linear time."""

import random
import timeit

from course_registration_sorting.graph import Graph, is_topological_order

LEVELS = 50  # edges only go to later levels (like semesters), so DFS depth stays under 50


def random_dag(n_vertices: int, n_edges: int) -> Graph:
    block = n_vertices // LEVELS
    graph = Graph()
    # shuffled, so DFS does not just follow index order
    for v in random.sample(range(n_vertices), n_vertices):
        graph.add_vertex(str(v))
    for _ in range(n_edges):
        u = random.randrange(n_vertices - block)
        v = random.randrange((u // block + 1) * block, n_vertices)
        graph.add_edge(str(u), str(v))
    return graph


def main() -> None:
    random.seed(3364)
    print(f"{'V':>7} {'E':>8} {'V+E':>8} {'ms':>8} {'ns/(V+E)':>9}")
    for k in range(7):
        n_vertices = 1000 * 2**k
        n_edges = 4 * n_vertices
        graph = random_dag(n_vertices, n_edges)
        assert is_topological_order(graph.vertices(), graph.edges(), graph.topological_sort())

        best = min(timeit.repeat(graph.topological_sort, number=1, repeat=3))
        size = n_vertices + n_edges
        ns_per_element = best * 1e9 / size
        print(f"{n_vertices:>7} {n_edges:>8} {size:>8} {best * 1e3:>8.1f} {ns_per_element:>9.0f}")


if __name__ == "__main__":
    main()
