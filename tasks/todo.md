# Todo: CS 3364 Project 2 — Course order by DFS topological sort

Full design and rationale: [plan.md](plan.md)

## Phase 1: Algorithm and data

### Task 1: Graph ADT + DFS pre/post + topological sort (S)
- [x] `dfs()` returns pre/post numbers from one shared clock; every edge u→v has post[u] > post[v] on a DAG
- [x] `topological_sort()` returns every vertex once, ordered by decreasing post; first vertex is a source
- [x] Cycle or self-loop raises `CycleError`
- [x] Verify: `uv run python -m unittest discover -s tests` (empty, single, chain, diamond, disconnected,
      hand-checked pre/post, cycle, self-loop) — 15 tests pass
- Files: `src/course_registration_sorting/graph.py`, `tests/test_graph.py` — Deps: none

### Task 2: Course adjacency list (S)
- [x] `PREREQS` (course → prerequisites, as the handout lists them) and `TITLES` have the same 29 keys
- [x] `course_graph()` flips them into prerequisite → course edges: 29 vertices, 30 edges
- [x] Resulting order passes `is_topological_order`; first course has no prerequisites
- [x] Verify: unittest suite — 19 tests pass
- Files: `src/course_registration_sorting/courses.py`, `tests/test_courses.py` — Deps: 1

### Task 3: main.py (XS)
- [x] `main()` prints numbered course order with pre/post numbers and a "30 prerequisites respected" line
- [x] Entry point moved to `main.py`; pyproject script and README updated
- [x] Verify: `uv run course-registration-sorting` prints 29 lines + check line
- Files: `main.py`, `__init__.py`, `pyproject.toml`, `README.md` — Deps: 2

### Checkpoint A
- [x] All tests pass; program output correct on course data
- [ ] User reviews the ordering before the report uses it

## Phase 2: Experiments and report

### Task 4: Timing experiment (S)
- [x] `scripts/benchmark.py`: layered random DAGs, V = 1k…64k, E ≈ 4V, fixed seed, best of 3
- [x] Asserts `is_topological_order`; prints V, E, V+E, ms, ns per (V+E)
- [x] Verify: `uv run python scripts/benchmark.py` finishes in about 1 s
- Files: `scripts/benchmark.py` — Deps: 1

### Task 5: Report (.docx) (M)
- [x] Sections: problem interpretation, methodology, experimental results, conclusions,
      future work, team considerations (placeholders for names/roles), appendices on running the code and full source
- [x] Tables pasted from real program and benchmark output
- [x] Verify: rendered to PDF and checked page by page; passes Word schema validation
- Files: `report/Project2_Report.docx` — Deps: 3, 4

### Checkpoint B
- [x] Tests pass, program and benchmark run clean
- [x] Report has all 4 required components + future work + team section
- [ ] User fills in team names/roles and reviews before submitting
