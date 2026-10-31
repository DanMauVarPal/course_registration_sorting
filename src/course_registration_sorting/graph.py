"""Directed graph ADT with DFS-based topological ordering."""


class CycleError(ValueError):
    """Raised when DFS finds a back edge, so no topological order exists."""

    def __init__(self, v: str, u: str) -> None:
        super().__init__(f"cycle found: edge {v} -> {u} leads back to an unfinished vertex")
        self.edge = (v, u)


class Graph:
    """Directed graph stored as an adjacency list: vertex -> vertices it has edges to."""

    def __init__(self, adjacency: dict[str, list[str]] | None = None) -> None:
        self._adj: dict[str, list[str]] = {}
        for v, neighbors in (adjacency or {}).items():
            self.add_vertex(v)
            for u in neighbors:
                self.add_edge(v, u)

    def add_vertex(self, v: str) -> None:
        self._adj.setdefault(v, [])

    def add_edge(self, v: str, u: str) -> None:
        self.add_vertex(v)
        self.add_vertex(u)
        self._adj[v].append(u)

    def vertices(self) -> list[str]:
        return list(self._adj)

    def neighbors(self, v: str) -> list[str]:
        return self._adj[v]

    def edges(self) -> list[tuple[str, str]]:
        return [(v, u) for v, neighbors in self._adj.items() for u in neighbors]

    def dfs(self) -> tuple[dict[str, int], dict[str, int]]:
        """Depth-first search over every vertex; returns the (pre, post) numbers."""
        self.pre: dict[str, int] = {}
        self.post: dict[str, int] = {}
        self.clock = 1
        self.visited = {v: False for v in self.vertices()}

        for v in self.vertices():
            if not self.visited[v]:
                self.explore(v)
        return self.pre, self.post

    def explore(self, v: str) -> None:
        """Visit everything reachable from v. Called by dfs(), which sets up the state."""
        # shortcut: recursion depth = longest path; Python stops near 1000 frames, use an explicit stack for deeper graphs.
        self.visited[v] = True
        self.previsit(v)

        for u in self.neighbors(v):
            if not self.visited[u]:
                self.explore(u)
            elif u not in self.post:  # back edge: u is still on the current DFS path
                raise CycleError(v, u)

        self.postvisit(v)

    def previsit(self, v: str) -> None:
        self.pre[v] = self.clock
        self.clock += 1

    def postvisit(self, v: str) -> None:
        self.post[v] = self.clock
        self.clock += 1

    def topological_sort(self) -> list[str]:
        """Vertices by decreasing post number: on a DAG every edge v -> u has post[v] > post[u]."""
        _, post = self.dfs()
        return sorted(post, key=post.get, reverse=True)


def is_topological_order(vertices: list[str], edges: list[tuple[str, str]], order: list[str]) -> bool:
    """True if order lists each vertex exactly once and every edge v -> u has v before u."""
    if sorted(order) != sorted(vertices):
        return False
    position = {v: i for i, v in enumerate(order)}
    return all(position[v] < position[u] for v, u in edges)
