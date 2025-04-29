from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        # Undirected graph: add both ways
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_recursive(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# Example usage
g = Graph()
edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (5, 6)]

for u, v in edges:
    g.add_edge(u, v)

print("DFS (Recursive):")
g.dfs_recursive(0)

print("\nBFS:")
g.bfs(0)
