from collections import deque


def answer(x, lst):
    print(x)
    print(*lst)


def solution(n, k):
    if n >= k:
        answer(n - k, [x for x in range(n, k - 1, -1)])
        return

    inf = max(n, k) + max(n, k) // 2 + 1
    q = deque([(n, [])])
    visited = [-1] * inf
    visited[n] = 0

    while q:
        c, step = q.popleft()
        length = len(step)
        if c == k:
            answer(length, [n] + step)
            return
        if length > visited[c]:
            continue
        for x in [c * 2, c - 1, c + 1]:
            if 0 <= x < inf and (visited[x] == -1 or length + 1 < visited[x]):
                q.append((x, step + [x]))
                visited[x] = length + 1


n, k = map(int, input().split())
solution(n, k)