import collections
import copy
import itertools
import sys
input = sys.stdin.readline


def calculate_area_size():
    """안전 영역의 넓이 확인

    :return: 안전 영역의 넓이"""

    q = collections.deque(virus)
    check_board = copy.deepcopy(board)

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 영역 밖이거나 빈 영역이 아닌 경우 판단하지 않음
            if nx < 0 or nx >= n or ny < 0 or ny >= m or check_board[nx][ny] != 0:
                continue
            check_board[nx][ny] = 2
            q.append((nx, ny))

    # 안전 영역(0의 개수) 확인
    global answer
    cnt = 0
    for c in check_board:
        cnt += c.count(0)
    answer = max(answer, cnt)


answer = 0
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

blank, virus = [], []
for x in range(n):
    for y in range(m):
        if board[x][y] == 0:
            blank.append((x, y))
        elif board[x][y] == 2:
            virus.append((x, y))

for blank in itertools.combinations(blank, 3):
    # 벽 3개 설치
    for wx, wy in blank:
        board[wx][wy] = 1
    # 안전 영역 넓이 확인
    calculate_area_size()
    # 벽 3개 제거
    for wx, wy in blank:
        board[wx][wy] = 0
        
print(answer)