import unittest

from course_registration_sorting.courses import PREREQS, TITLES, course_graph
from course_registration_sorting.graph import is_topological_order


class CoursesTest(unittest.TestCase):
    def test_every_course_has_a_title(self):
        self.assertEqual(len(PREREQS), 29)
        self.assertEqual(PREREQS.keys(), TITLES.keys())

    def test_graph_has_no_unknown_prerequisites(self):
        # a typo'd prerequisite would show up as a 30th vertex
        graph = course_graph()
        self.assertEqual(graph.vertices(), list(PREREQS))
        self.assertEqual(len(graph.edges()), 30)

    def test_order_respects_every_prerequisite(self):
        order = course_graph().topological_sort()
        edges = [(prereq, course) for course, prereqs in PREREQS.items() for prereq in prereqs]
        self.assertTrue(is_topological_order(list(PREREQS), edges, order))

    def test_highest_post_number_has_no_prerequisites(self):
        self.assertEqual(PREREQS[course_graph().topological_sort()[0]], [])


if __name__ == "__main__":
    unittest.main()
