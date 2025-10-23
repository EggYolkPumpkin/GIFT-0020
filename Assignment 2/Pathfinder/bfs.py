from collections import deque
from node import Node


def bfs(start, end):
    queue = deque([start])
    visited = set()
    came_from = {}
    visit_history = []
    start.f_score = 0

    while queue:
        current = queue.popleft()
        visit_history.append(current)
        if current == end:
            return reconstruct_path(came_from, current), visit_history

        visited.add(current)

        for neighbor in current.get_neighbors():
            if neighbor not in visited and neighbor not in queue and neighbor.type != 'wall':
                queue.append(neighbor)
                came_from[neighbor] = current
                neighbor.f_score = current.f_score + 1

    return None  # No path found


def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path
