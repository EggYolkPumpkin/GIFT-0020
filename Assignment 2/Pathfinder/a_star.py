from collections import deque
from node import Node


def a_star(start, end):
    queue = deque([start])
    visited = set()
    came_from = {}
    visit_history = []
    start.f_score = 0
    start.g_score = abs(start.x - end.x) + abs(start.y - end.y)
    while queue:
        current = queue.popleft()
        visit_history.append(current)
        if current == end:
            return reconstruct_path(came_from, current), visit_history

        visited.add(current)

        for neighbor in current.get_neighbors():
            if neighbor not in visited and neighbor.type != 'wall':
                if neighbor.g_score == float('inf'):
                    neighbor.g_score = abs(neighbor.x - end.x) + abs(neighbor.y - end.y)
                if neighbor.f_score == float('inf') or neighbor.f_score > current.f_score + 1:
                    neighbor.f_score = current.f_score + 1
                    came_from[neighbor] = current
                if neighbor not in queue:
                    queue.append(neighbor)

        queue = deque(sorted(queue, key=lambda t: t.f_score + t.g_score, reverse=False))
    return None  # No path found


def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path
