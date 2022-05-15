# BFS는 너비 우선 탐색 알고리즘이다.
# DFS는 최대한 멀리 있는 노드를 우선으로 탐색하는 방식으로 동작한다고 했는데, BFS는 그 반대다.
# BFS 구현에서는 선입선출 방식인 '큐' 자료구조를 이용하는 것이 정석이다.

# (1) 탐색 시작 노드를 큐에 삽입 및 방문 처리
# (2) 큐에서 노드를 꺼내 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입 및 방문 처리
# (3) (2)번의 과정을 더 이상 수행할 수 없을 때까지 반복

# BFS의 구현은 deque 라이브러리를 사용하는 것이 좋다. 탐색 수행 시간은 O(N)
# 일반적인 경우 실제 수행 시간은 DFS보다 좋은 편이다. (재귀 함수는 컴퓨터 시스템의 동작 특성상 느릴 수 있음)

from collections import deque


# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],  # 1번 노드 -> 2, 3, 8번 노드와 연결
    [1, 7],     # 2번 노드 -> 1, 7번 노드와 연결
    [1, 4, 5],  # ...
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]      # 8번 노드 -> 1, 7번 노드와 연결
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
bfs(graph, 1, visited)

# --------------------------------------------------------------------------------------------------------------------
# DFS: 스택 -> 재귀 함수 이용
# BFS: 큐 -> 큐 자료구조 이용(deque)

# 1차원 배열이나 2차원 배열 또한 그래프 형태로 생각하면 DFS와 BFS를 이용하여 수월하게 문제를 풀 수 있다.
