def dfs(graph, start):
 stack = [start]
 visited = set()
 while stack:
    node = stack.pop(0)
    if node not visited:
        visited.add(node)
        stack.extend(graph[node])
    return visited
graph = {1: [2, 3], 2: [4], 3: [4], 4: []}
print(dfs(graph, 1))
