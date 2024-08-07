import heapq


INF = int(1e9)


def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)
    
    for a, b in roads:
        graph[a].append((b, 1))
        graph[b].append((a, 1))
        
    q = []
    heapq.heappush(q, (0, destination))
    distance[destination] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for v, c in graph[now]:
            if (cost := dist + c) < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))
                
    for source in sources:
        answer.append(distance[source] if distance[source] != INF else -1)
            
    return answer
