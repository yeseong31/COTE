def solution(n, s):
    if n > s:
        return [-1]
    
    answer = [s // n] * n
    for i in range(s % n):
        answer[n - 1] += 1
        n -= 1
    return answer
