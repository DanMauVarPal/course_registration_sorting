# Todo: CS 3364 Project 2 — Course order by DFS topological sort

Full design and rationale: [plan.md](plan.md)

## Phase 1: Algorithm and data

### Task 1: Graph ADT + DFS pre/post + topological sort (S)
- [ ] `dfs()` returns pre/post numbers from one shared clock; every edge u→v has post[u] > post[v] on a DAG
- [ ] `topological_sort()` returns every vertex once, ordered by decreasing post; first vertex is a source
- [ ] Cycle or self-loop raises `CycleError`
- [ ] Verify: `uv run python -m unittest discover -s tests` (empty, single, chain, diamond, disconnected,
      hand-checked pre/post, cycle, self-loop)
- Files: `src/course_registration_sorting/graph.py`, `tests/test_graph.py` — Deps: none

### Task 2: Course adjacency list (S)
- [ ] `COURSES` has 29 keys and 30 edges; `TITLES` has the same 29 keys
- [ ] Test compares `COURSES` edges against the prerequisites as written in the assignment
- [ ] Resulting order passes `is_topological_order` against that independent list
- [ ] Verify: unittest suite; CS 3364 after CS 2413, CS 1382, MATH 2360
- Files: `src/course_registration_sorting/courses.py`, `tests/test_courses.py` — Deps: 1

### Task 3: main.py (XS)
- [ ] `main()` prints numbered course order with pre/post numbers and a "30 prerequisites respected" line
- [ ] Entry point moved to `main.py`; pyproject script and README updated
- [ ] Verify: `uv run course-registration-sorting` prints 29 lines + check line
- Files: `main.py`, `__init__.py`, `pyproject.toml`, `README.md` — Deps: 2

### Checkpoint A
- [ ] All tests pass; program output correct on course data
- [ ] User reviews the ordering before the report uses it

## Phase 2: Experiments and report

### Task 4: Timing experiment (S)
- [ ] `scripts/benchmark.py`: layered random DAGs, V = 1k…64k, E ≈ 4V, fixed seed, best of 3
- [ ] Asserts `is_topological_order`; prints V, E, V+E, ms, ns per (V+E)
- [ ] Verify: `uv run python scripts/benchmark.py` finishes in well under a minute
- Files: `scripts/benchmark.py` — Deps: 1

### Task 5: Report (.docx) (M)
- [ ] Sections: problem interpretation, methodology, experimental results, conclusions,
      future work, team considerations (placeholders for names/roles), appendix on running the code
- [ ] Tables pasted from real program and benchmark output
- [ ] Verify: open/render the .docx and cross-check numbers
- Files: `report/Project2_Report.docx` — Deps: 3, 4

### Checkpoint B
- [ ] Tests pass, program and benchmark run clean
- [ ] Report has all 4 required components + future work + team section
- [ ] User fills in team names/roles and reviews before submitting
