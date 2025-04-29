# Simple Prim's Algorithm Example

# Graph as an adjacency list: (node, weight)
graph = {
    0: [(1, 1), (2, 3)],
    1: [(0, 1), (2, 1), (3, 4)],
    2: [(0, 3), (1, 1), (3, 1)],
    3: [(1, 4), (2, 1)]
}

import heapq

def prim_mst(graph, start):
    visited = set()
    mst = []
    min_heap = [(0, start, -1)]  # (weight, current_node, parent)

    while min_heap and len(visited) < len(graph):
        weight, node, parent = heapq.heappop(min_heap)
        if node in visited:
            continue
        visited.add(node)
        if parent != -1:
            mst.append((parent, node, weight))
        for neighbor, wt in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (wt, neighbor, node))

    return mst

# Run the algorithm
mst = prim_mst(graph, 0)

# Print result
print("Edges in the MST:")
for u, v, w in mst:
    print(f"{u} - {v} (Weight: {w})")
