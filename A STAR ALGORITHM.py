import heapq

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position  # (x, y)
        self.parent = parent      # Previous node
        self.g = g                # Cost from start to current node
        self.h = h                # Heuristic cost to goal
        self.f = g + h            # Total cost

    def __lt__(self, other):  # For priority queue
        return self.f < other.f

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(grid, start, goal):
    open_list = []
    closed_set = set()

    start_node = Node(start, None, 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        closed_set.add(current_node.position)

        # 4 possible directions (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = current_node.position[0] + dx, current_node.position[1] + dy
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0:
                neighbor = (x, y)
                if neighbor in closed_set:
                    continue
                g_cost = current_node.g + 1
                h_cost = heuristic(neighbor, goal)
                new_node = Node(neighbor, current_node, g_cost, h_cost)
                heapq.heappush(open_list, new_node)

    return None  # No path found

# Example Grid: 0 = empty, 1 = obstacle
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

path = a_star_search(grid, start, goal)
print("A* Path:", path)
