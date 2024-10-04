def bfs(graph, start):
 visited = set()
 queue = [(start, 0)]
 level = {}
 while queue:
    node, depth = queue.pop()
    if node not in visited:
        visited.add(node)
        level[node] = depth

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, depth)) 
 return level

graph = {1: [2, 3], 2: [4], 3: [5], 4: [], 5: []}
print(bfs(graph, 1))