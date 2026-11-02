"""Directed graph ADT with DFS-based topological ordering."""


class CycleError(ValueError):
    """Raised when DFS finds a back edge, so no topological order exists."""

    def __init__(self, v: str, u: str) -> None:
        super().__init__(f"cycle found: edge {v} -> {u} leads back to an unfinished vertex")
        self.edge = (v, u)


class Graph:
    """Directed graph stored as an adjacency list: vertex -> vertices it has edges to."""

    # adjacency dictionary or nothing param
    def __init__(self, adjacency: dict[str, list[str]] | None = None) -> None:
        # local attribute adjecency dictionary
        self._adj: dict[str, list[str]] = {}

        # adjecency dict poblation
        # v: "CS 1412"
        # directed neighbors: ["CS 2350", "CS 2413"]
        for v, neighbors in (adjacency or {}).items():
            # Add "CS 1412" to local dict
            self.add_vertex(v)
            
            # u: "CS 2350"
            # create directed edge v -> u
            for u in neighbors:
                self.add_edge(v, u)

    # inserts {key, value} into adj dict if it doesn't exist
    # "v": []
    def add_vertex(self, v: str) -> None:
        self._adj.setdefault(v, [])


    # appends "u" to "v".directedNode[] key in the adj dict
    def add_edge(self, v: str, u: str) -> None:
        # inserts "v": []
        # redundancy check
        self.add_vertex(v)
        # inserts "v": []
        self.add_vertex(u)
        # appends "v": [..., "u"]
        self._adj[v].append(u)

    # returns list of vertices (keys only) on the adj dict
    def vertices(self) -> list[str]:
        return list(self._adj)

    # returns list of neighbors of vertex "v"
    # v -> neighbors
    def neighbors(self, v: str) -> list[str]:
        return self._adj[v]

    # returns list of edges (v, u)
    def edges(self) -> list[tuple[str, str]]:
        return [(v, u) for v, neighbors in self._adj.items() for u in neighbors]

    # pre- and post- visit operations
    # register clock cycle number
    def previsit(self, v: str) -> None:
        self.pre[v] = self.clock
        self.clock += 1
    def postvisit(self, v: str) -> None:
        self.post[v] = self.clock
        self.clock += 1

    def dfs(self) -> tuple[dict[str, int], dict[str, int]]:
        """Depth-first search over every vertex; returns the (pre, post) numbers."""
        # pre- & post-numbers dicts for all vertices
        # "v": pre-number
        self.pre: dict[str, int] = {}
        # "v": post-number
        self.post: dict[str, int] = {}
        
        # number register
        self.clock = 1

        # vertex dict with all v.visited = False
        self.visited = {v: False for v in self.vertices()}

        # gets "v" from vertices list
        for v in self.visited:
            # checks if vertex wasn't explored
            if not self.visited[v]:
                # explores if not visited
                self.explore(v)
        
        # returns pre- & post-numbers dicts
        return self.pre, self.post

    def explore(self, v: str) -> None:
        """Visit everything reachable from v. Called by dfs(), which sets up the state."""
        
        self.visited[v] = True
        
        self.previsit(v)

        for u in self.neighbors(v):
            if not self.visited[u]:
                self.explore(u)
            
            # checks for SCC's through back edges
            # DFA shouldn't have reducable SCC into meta-nodes
            elif u not in self.post:
                raise CycleError(v, u)

        self.postvisit(v)

    def topological_sort(self) -> list[str]:
        """Vertices by decreasing post number: on a DAG every edge v -> u has post[v] > post[u]."""
        # post-numbers dict storing
        _, post = self.dfs()

        # return list of node names (post dict keys)
        # decreasing post-number
        return sorted(post, key=post.get, reverse=True)


# params are:
# vertices: courses
# edges: prereq -> course
# order: course topological order to check
def is_topological_order(
    vertices: list[str], edges: list[tuple[str, str]], order: list[str]
) -> bool:
    """True if order lists each vertex exactly once and every edge v -> u has v before u."""
    # verifies that vertices are the same ones as in order
    if sorted(order) != sorted(vertices):
        return False

    # creates dict with nodes in order
    # "v": order_number
    position = {v: i for i, v in enumerate(order)}

    # all v come before u in edges
    # prereq -> course True
    # course -> prereq False
    return all(position[v] < position[u] for v, u in edges)
