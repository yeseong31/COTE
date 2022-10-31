from collections import deque


def solution(A, B):
    answer = 0

    A = deque(sorted(A))
    B = deque(sorted(B))

    i = j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            answer += 1
            i += 1
            j += 1
        else:
            j += 1

    return answer
