from collections import deque
from node import Node


def dfs(start, end):
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
        append_list = deque([])
        for neighbor in current.get_neighbors():
            if neighbor not in visited and neighbor.type != 'wall':
                came_from[neighbor] = current
                neighbor.f_score = current.f_score + 1
                if neighbor in queue:
                    queue.remove(neighbor)
                append_list.append(neighbor)
        queue = append_list + queue
    return None  # No path found


def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path
