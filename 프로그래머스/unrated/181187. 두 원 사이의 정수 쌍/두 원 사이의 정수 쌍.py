def solution(r1, r2):
    answer = 0
    for w in range(1, r2):
        h2 = (r2 ** 2 - w ** 2) ** 0.5
        if w >= r1:
            answer += int(h2) + 1
            continue
        h1 = (r1 ** 2 - w ** 2) ** 0.5
        answer += int(h2) - int(h1)
        if h1 == int(h1):
            answer += 1
    return 4 * (answer + 1)
