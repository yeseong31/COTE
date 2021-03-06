# ---------------------------------------------------------------------------------------------------------------------
# <개선된 다익스트라 알고리즘>
# 최악의 경우에도 시간 복잡도 O(ElogV)를 보장하는 알고리즘 (E: 간선의 개수, V: 노드의 개수)
# 간단한 다익스트라 알고리즘에서 '최단 거리가 가장 짧은 노드를 선형적으로 찾는 것'을 개선하여 탐색 시간을 줄인 방법
# 힙 자료구조를 사용하여 특정 노드까지의 최단 거리에 대한 정보를 힙에 담아 처리하므로
# 출발 노드로부터 가장 거리가 짧은 노드를 더욱 빠르게 찾을 수 있다.

# ---------------------------------------------------------------------------------------------------------------------
# <힙 자료구조>
# '우선순위 큐'를 구현하기 위하여 사용하는 자료구조 중 하나

# 우선순위 값을 표현할 때는 일반적으로 정수형 자료형의 변수가 사용된다.
# 우선순위 큐를 구현할 때는 파이썬의 우선순위 큐 라이브러리(최소 힙)룰 그대로 사용하면 된다.
# 최소 힙을 최대 힙처럼 사용하기 위해서는 우선순위에 해당하는 값에 음수 부호(-)를 붙여 사용하면 된다.

# 힙 자료구조의 전체 연산 횟수에 대한 시간 복잡도는 O(NlogN)
# 힙 정렬 구현 소스코드는 heapq_lib.py 를 참고하도록 하자.

# ---------------------------------------------------------------------------------------------------------------------
# '단순한 다익스트라 알고리즘'의 소스코드와 비교하면 get_smallest_node()라는 함수를 작성할 필요가 없다는 것이 특징이다.
# '최단 거리가 가장 짧은 노드'를 선택하는 과정을 다익스트라 최단 경로 함수 안에서
# 우선순위 큐를 이용하는 방식으로 대체할 수 있기 때문이다.

# ---------------------------------------------------------------------------------------------------------------------
import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선 개수
n, m = map(int, input().split())
# 시작 노드 번호
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for _ in range(n + 1)]
# 최단 거리 테이블
distance = [INF] * (n + 1)

# 모든 간선 정보 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# 다익스트라 최단 거리 알고리즘(개선 버전 - BFS 이용)
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있다면 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                # i[0]로 가는 비용이 cost라는 뜻
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, '무한'이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

# ---------------------------------------------------------------------------------------------------------------------

# 전체 다익스트라 최단 경로 알고리즘은 E개의 원소를 우선순위 큐에 넣었다 모두 빼내는 연산과 매우 유사하다고 볼 수 있다.
# 다익스트라 알고리즘의 경우 최대 E개의 간선 데이터를 힙에 넣었다가 다시 빼는 것으로 볼 수 있으므로 O(ElogE)이다.
# 이때 중복 간선을 포함하지 않는 경우, E는 항상 V^2보다 작다. 모든 노드끼리 서로 다 연결되어 있다고 했을 때
# 간선의 개수를 약 V^2로 볼 수 있고 E는 항상 V^2 이하이기 때문이다.
# 다시 말해 logE < log(V^2) = 2logV, 즉 O(logE) = O(logV)이다.
# 따라서 개선된 다익스트라 알고리즘의 전체 시간 복잡도를 O(ElogV)로 볼 수 있다.

# 다익스트라 최단 경로 알고리즘은 우선순위 큐를 이용한다는 점에서 우선순위 큐를 필요로 하는 다른 문제 유형과도 흡사하다.
# 예를 들어 그래프 문제로 유명한 최소 신장 트리 문제를 풀 때에도 Prim 알고리즘 등이 다익스트라 알고리즘과 비슷하다.

# ---------------------------------------------------------------------------------------------------------------------
# [파이썬 알고리즘 인터뷰]ver (378p)


def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    q = [(0, k)]
    dist = defaultdict(int)

    while q:
        time, node = heapq.heappop(q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(q, (alt, v))

    if len(dist) == n:
        return max(dist.values())
    return -1

