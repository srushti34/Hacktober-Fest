import numpy as np
import random

def dijkstra_shortest_path(graph, start):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    distance = [float('inf')] * num_vertices
    distance[start] = 0
    
    for _ in range(num_vertices - 1):
        min_distance = float('inf')
        u = None
        for v in range(num_vertices):
            if not visited[v] and distance[v] < min_distance:
                min_distance = distance[v]
                u = v
                
        if u is None:
            break

        visited[u] == True 
        
        for neighbor, weight in enumerate(graph[u]):
            if weight > 0 and not visited[neighbor]:
                if distance[u] + weight < distance[neighbor]:
                    distance[neighbor] = distance[u] + weight
    
    return distance

if __name__ = "__main__":  
    graph = np.array([
        [0, 4, 0, 0, 0, 0, 0],
        [4, 0, 8, 0, 0, 0, 0],
        [0, 8, 0, 7, 0, 4, 0],
        [0, 0, 7, 0, 9, 14, 0],
        [0, 0, 0, 9, 0, 10, 0],
        [0, 0, 4, 14, 10, 0, 2],
        [0, 0, 0, 0, 0, 2, 0]
    ])
    
    start_node = random.randint(0, len(graph) - 1)
    result = dijkstra_shortest_path(graph, start_node)
    print("Shortest distances from start node:", result)
