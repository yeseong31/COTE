import heapq


def solution(N, road, K):
    INF = int(1e9)
    answer = 0

    graph = [[] for _ in range(N + 1)]
    dist = [INF] * (N + 1)
    start = 1

    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for v in graph[now]:
            cost = d + v[1]
            if cost < dist[v[0]]:
                dist[v[0]] = cost
                heapq.heappush(q, (cost, v[0]))

    for i in range(1, N + 1):
        if dist[i] <= K:
            answer += 1

    return answer