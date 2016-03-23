#!/usr/bin/env python


"""
    Expected structure for graphs with vertex id and adjacency:

    { 'A': set(['B','C']),
      'B': set(['A']),
      'C': set(['A'])
    }

    Where start is the vertex id of the root
"""


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited
