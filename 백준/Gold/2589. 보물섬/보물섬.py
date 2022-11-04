import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [input() for _ in range(n)]

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)


def bfs(x, y):
    q = deque([(x, y)])
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    count = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] == 'L' and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                count = max(count, visited[nx][ny])
                q.append((nx, ny))
    return count - 1


answer = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'L':
            answer = max(answer, bfs(i, j))
print(answer)