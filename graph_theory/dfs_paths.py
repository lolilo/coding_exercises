graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def dfs_paths(graph, start, goal):
    paths = []
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                paths.append(path + [next])
            else:
                stack.append((next, path + [next]))
    return paths


def dfs_paths_recursive(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        return [path]
    paths = []
    for next in graph[start] - set(path):
        extended_paths = dfs_paths_recursive(graph, next, goal, path + [next])
        for extended_path in extended_paths:
            paths.append(extended_path)
    return paths


print dfs_paths(graph, 'A', 'F')  # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
print dfs_paths_recursive(graph, 'C', 'F') # [['C', 'F'], ['C', 'A', 'B', 'E', 'F']]
