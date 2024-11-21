import heapq
def prim(graph, start):
    mst = []
    visited = set()
    min_heap = [(0, start)]  # (weight, vertex)

    while min_heap:
        weight, vertex = heapq.heappop(min_heap)
        if vertex not in visited:
            visited.add(vertex)
            mst.append((weight, vertex))

            for neighbor, edge_weight in graph[vertex]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, neighbor))
    return mst[1:]  
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('C', 1), ('D', 4)],
    'C': [('A', 3), ('B', 1), ('D', 2)],
    'D': [('B', 4), ('C', 2)]
}

mst = prim(graph, 'A')
print("Minimum Spanning Tree:", m
