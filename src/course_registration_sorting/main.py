from course_registration_sorting.courses import TITLES, course_graph
from course_registration_sorting.graph import is_topological_order


def main() -> None:
    graph = course_graph()
    order = graph.topological_sort()

    for i, course in enumerate(order, 1):
        print(f"{i:2}. {course} - {TITLES[course]} (pre {graph.pre[course]}, post {graph.post[course]})")

    valid = is_topological_order(graph.vertices(), graph.edges(), order)
    print(f"\nAll {len(graph.edges())} prerequisites respected: {valid}")


if __name__ == "__main__":
    main()
