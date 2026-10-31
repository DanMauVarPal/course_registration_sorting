# Plan: CS 3364 Project 2 — Course order by DFS topological sort

## Context
The assignment (`Project2.md`, transcript of `Project2.doc`) asks for a prototype **graph ADT** with a
**DFS-based topological sort**, applied to the 29 CS-major courses and their prerequisites to produce
a valid order for taking them. The graded deliverable is a **report** (Word .docx) with: problem
interpretation, methodology, experimental results, conclusions, plus future work and team
considerations (needed for the top rubric band). Grading also weighs design correctness "with
flexibilities" (40), implementation correctness (40), and readability (10).

Repo today: uv project, Python ≥3.14, no dependencies, `src/course_registration_sorting/__init__.py`
has a placeholder `main()` wired to the `course-registration-sorting` script. Nothing to reuse yet.

User decisions: report as **.docx**; **team** project (leave a roles section to fill in); results
include **course ordering + timing test**; course data is a **Python adjacency list in its own module**
imported by `main.py`; DFS follows the **pre/post clock algorithm** below, and the order is the
vertices sorted by **decreasing post number** (sources get the highest post numbers).

```
previsit(v):  pre[v] = clock++          explore(G, v): v.visited = true; previsit(v)
postvisit(v): post[v] = clock++                        for each edge (v, u): if !u.visited: explore(G, u)
dfs(G): all v unvisited; for all v in V: if !v.visited: explore(G, v)          postvisit(v)
```

## Design decisions
- **Graph ADT** (`graph.py`): class wrapping an adjacency list `dict[str, list[str]]` (insertion-ordered,
  so output is deterministic). Methods: `add_vertex`, `add_edge(u, v)`, `vertices()`, `neighbors(v)`,
  `edges()`, `dfs() -> (pre, post)`, `topological_sort()`. `dfs`, `explore`, `previsit`, `postvisit`
  keep the pseudocode's names and shape (recursive), so the code reads like the lecture.
- **Topological order** = `sorted(vertices, key=post, reverse=True)`. For every edge u→v in a DAG,
  post[u] > post[v], so prerequisites come first and the highest post number lands on a source.
- **Cycle check** (2 lines, DPV back-edge test): in `explore`, an edge to a vertex that is visited but has
  no post number yet is a back edge ⇒ raise `CycleError(v, u)`. Without it a bad graph would silently
  give a wrong order.
- **Recursion depth** = longest prerequisite chain (6 for the course data). Python allows ~1000 frames;
  recorded as a `shortcut:` comment in `explore` (switch to an explicit stack for deeper graphs).
- `is_topological_order(edges, order)`: every vertex once, every edge u→v has u before v. Oracle for
  tests and the benchmark.
- **Course data** (`courses.py`): `COURSES` = adjacency list, prerequisite → courses it unlocks
  (e.g. `"CS 1411": ["CS 1412", "CS 1382"]`), every course a key (empty list if it unlocks nothing);
  `TITLES` = code → name for printing. Sanity numbers: 29 courses, 30 edges.
- **Tests**: stdlib `unittest`, no new dependency.
- **Report**: generated once with the `anthropic-skills:docx` skill; no doc library added to the project.

## Files
- `src/course_registration_sorting/graph.py` — Graph, CycleError, is_topological_order (new)
- `src/course_registration_sorting/courses.py` — `COURSES`, `TITLES` (new)
- `src/course_registration_sorting/main.py` — `main()` (new); placeholder removed from `__init__.py`
- `pyproject.toml` — script entry → `course_registration_sorting.main:main`, description
- `scripts/benchmark.py` — timing experiment (new)
- `tests/test_graph.py`, `tests/test_courses.py` (new)
- `README.md` — how to run
- `report/Project2_Report.docx` (new)
- `tasks/plan.md`, `tasks/todo.md` — this plan + checklist, per the planning skill (new)

## Tasks

### Task 0: Record the plan (XS)
Write `tasks/plan.md` (this document) and `tasks/todo.md` (checklist of Tasks 1–5 + checkpoints).
**Done when:** both files exist; nothing else changed.

### Task 1: Graph ADT + DFS pre/post + topological sort (S)
**Acceptance:**
- [ ] `dfs()` returns pre/post numbers from one shared clock; every edge u→v has post[u] > post[v] on a DAG
- [ ] `topological_sort()` returns every vertex once, ordered by decreasing post; first vertex is a source
- [ ] Cycle or self-loop raises `CycleError`
**Verify:** `uv run python -m unittest discover -s tests` — cases: empty, single vertex, chain, diamond,
disconnected parts, a small graph with pre/post numbers checked by hand, cycle, self-loop.
**Files:** `graph.py`, `tests/test_graph.py`. **Deps:** none.

### Task 2: Course adjacency list (S) — highest risk: hand-inverting prerequisites
**Acceptance:**
- [ ] `COURSES` has 29 keys and 30 edges; `TITLES` has the same 29 keys
- [ ] Test holds the prerequisites exactly as the assignment writes them (course → its prereqs) and checks
      that the edges of `COURSES` are exactly those pairs reversed — catches any transcription slip
- [ ] Resulting order passes `is_topological_order` against that independent prerequisite list
**Verify:** unittest suite; spot-check CS 3364 comes after CS 2413, CS 1382, MATH 2360.
**Files:** `courses.py`, `tests/test_courses.py`. **Deps:** 1.

### Task 3: main.py (XS)
`main()` builds the Graph from `COURSES`, runs the sort, prints a numbered list
`1. CS 1411 - Programming Principles I (pre 1, post 12)` and a final line confirming all 30
prerequisites are respected. Move entry point to `main.py`, update pyproject script + README.
**Verify:** `uv run course-registration-sorting` prints 29 lines + check line.
**Files:** `main.py`, `__init__.py`, `pyproject.toml`, `README.md`. **Deps:** 2.

### Checkpoint A (after 1–3)
- [ ] All tests pass; program output correct on course data
- [ ] User reviews the ordering before the report uses it

### Task 4: Timing experiment (S)
`scripts/benchmark.py`: fixed seed; for V = 1k, 2k, 4k … 64k with E ≈ 4V, build a random **layered**
DAG (vertices spread over ~50 levels, edges only to later levels — like semesters, and keeps recursion
depth ≤ 50), time `topological_sort` with `time.perf_counter` (best of 3), assert
`is_topological_order`, print table: V, E, V+E, ms, ns per (V+E). Roughly flat last column = linear-ish
(DFS is O(V+E); the final sort by post adds O(V log V), noted in the report).
**Verify:** `uv run python scripts/benchmark.py` finishes in well under a minute.
**Files:** `scripts/benchmark.py`. **Deps:** 1.

### Task 5: Report (.docx) (M)
Using the docx skill, write `report/Project2_Report.docx`:
1. **Problem interpretation** — courses as vertices, prerequisite → course as directed edges, why it must
   be a DAG, what a valid order means, why sources get the highest post numbers.
2. **Methodology** — ADT interface, adjacency-list choice, DFS pseudocode with pre/post clock, ordering
   by decreasing post, back-edge cycle check, complexity, recursion-depth note.
3. **Experimental results** — full course order (table: #, code, title, pre, post), validity check, test
   list and results, timing table from Task 4 with interpretation.
4. **Conclusions**.
5. **Future work** — BFS/Kahn's algorithm, semester planning (group by level, credit-hour caps), loading
   other catalogs, iterative DFS for very deep graphs, more algorithms on the same ADT.
6. **Team considerations** — how the work split (ADT / data / tests / report) and how we coordinated;
   names and roles left as clearly marked placeholders for the team to fill in.
Appendix: how to run the code.
**Verify:** open the .docx (or render it to PDF/images) and check all sections, and that tables match
real program output (pasted, not hand-typed).
**Files:** `report/Project2_Report.docx`. **Deps:** 3, 4.

### Checkpoint B (done)
- [ ] Tests pass, program and benchmark run clean
- [ ] Report has all 4 required components + future work + team section
- [ ] User fills in team names/roles and reviews before submitting

## Risks
| Risk | Impact | Mitigation |
|---|---|---|
| Slip when inverting prerequisites into the adjacency list | High | Test compares against the assignment's prerequisite list as written; edge count 30 |
| Recursion limit on deep graphs | Low | Course depth is 6; benchmark uses bounded-depth DAGs; noted as future work |
| Timing noise on small sizes | Low | Best of 3, sizes doubling to 64k |
| Report numbers drift from code | Med | Paste results straight from program output |

## Verification (end to end)
```
uv run python -m unittest discover -s tests
uv run course-registration-sorting
uv run python scripts/benchmark.py
```
Then open `report/Project2_Report.docx` and cross-check its tables against the last two outputs.

## Not doing (unless asked)
Reading course lists from text files, semester-by-semester schedule, GUI, graph drawing, timing chart
(table only), BFS/other algorithms — the useful ones are listed as future work in the report.
No commits unless you ask.
