def solution(distance, scope, times):
    answer = distance

    for i in range(len(times)):
        rule = 'o' * times[i][0] + 'x' * times[i][1]
        l, r = sorted(scope[i])
        s = l % sum(times[i])

        for step in range(r - l + 1):
            if rule[s - 1] == 'o':
                answer = min(answer, l + step)
            s = s + 1 if s < len(rule) else 1

    return answer