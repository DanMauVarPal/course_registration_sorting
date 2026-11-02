# course_registration_sorting

CS 3364 Project 2: finds an order for taking the CS major courses so every prerequisite comes first,
using a DFS-based topological sort (vertices sorted by decreasing post number).

- `src/course_registration_sorting/graph.py` — graph ADT, DFS with pre/post numbers, topological sort
- `src/course_registration_sorting/courses.py` — the courses and their prerequisites
- `src/course_registration_sorting/main.py` — prints the course order

```
uv run course-registration-sorting                 # print the course order
uv run python -m unittest discover -s tests        # run the tests
uv run python scripts/benchmark.py                 # time the sort on random graphs, 1k to 64k vertices
```
