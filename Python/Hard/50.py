def floyd_warshall(graph):
 dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
 V = len(graph)
 for k in range(V):
    for i in range(V):
        for j in range(V)
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
 return dist
graph = [[0, 3, float('inf'), 7],
        [8, 0, 2, float('inf')],
        [5, float('inf'), 0, 1],
        [2, float('inf'), float('inf'), 0]]
print(floyd_warshall(graph))