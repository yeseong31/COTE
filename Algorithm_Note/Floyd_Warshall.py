# <플로이드 워셜 알고리즘>
# '플로이드 워셜 알고리즘'은 '모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우'에 사용할 수 있는 알고리즘이다.

# 플로이드 워셜 알고리즘 또한 다익스트라 알고리즘처럼 단계마다 '거쳐 가는 노드'를 기준으로 알고리즘을 수행하지만,
# 매번 방문하지 않은 노드 중에서 최단 거리를 갖는 노드를 찾을 필요가 없다는 점이 가장 큰 차이점이다.
# 노드의 개수가 N개일 때 알고리즘상으로 N번의 단계를 수행하며, 단계마다 O(N^2)의 연산을 통해 '현재 노드를 거쳐 가는' 모든 경로를 고려한다.
# 따라서 플로이드 워셜 알고리즘의 총시간 복잡도는 O(N^3)이다.

# 플로이드 워셜 알고리즘은 다익스트라 알고리즘과는 다르게 2차원 리스트에 '최단 거리' 정보를 저장한다.
# 모든 노드에 대해 다른 모든 노드로 가는 최단 거리 정보를 담아야 하기 때문이다.
# 또한 다익스트라 알고리즘은 그리디 알고리즘인데 플로이드 워셜 알고리즘은 다이나믹 프로그래밍이라는 특징이 있다.
# 노드의 개수 N만큼의 단계를 반복하며 '점화식에 맞게' 2차원 리스트를 갱신하기 때문이다.

# 각 단계에서는 해당 노드를 거쳐 가는 경우를 고려한다. 알고리즘에서는 현재 확인하고 있는 노드를 제외하고, (N - 1)개의 노드 중에서
# 서로 다른 노드 (A, B) 쌍을 선택한다. 이후에 A -> 1번 노드 -> B로 가는 비용을 확인한 뒤에 최단 거리를 갱신한다.
# 즉 (N-1 P 2)개의 쌍을 단계마다 반복해서 확인하면 된다. O(N-1 P 2)는 O(N^2)로 볼 수 있으므로 전체 시간 복잡도는 O(N^3)이다.
#     D(ab) = min( D(ab), D(ak) + D(kb) )       D(ab): 'a에서 b로 가는 최단 거리'
#         'A에서 B로 가는 최소 비용'과 'A에서 K를 거쳐 B로 가는 비용'을 비교하여 더 작은 값으로 갱신
# 즉 '바로 이동하는 거리'가 '특정 노드를 거쳐 이동하는 거리'보다 더 많은 비용을 가진다면 이를 더 짧은 것으로 갱신한다는 것이다.
# 따라서 전체적으로 3중 반복문을 이용하여 이 점화식에 따라 최단 거리 테이블을 갱신하면 된다.

# --------------------------------------------------------------------------------------------------------------------
INF = int(1e9)

# 노드 개수, 간선 개수
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받고, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INFINITY", end=' ')
        else:
            print(graph[a][b], end=' ')
    print()

# 입력 예시
# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2
# 출력 예시
# 0 4 8 6
# 3 0 7 9
# 5 9 0 4
# 7 11 2 0
