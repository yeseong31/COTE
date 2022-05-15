# 다이나믹 프로그래밍을 적용했을 때의 피보나치 수열 알고리즘의 시간 복잡도는 O(N)이다.
# f(1)을 구한 다음 그 값이 f(2)를 푸는 데 사용되고, f(2)의 값이 f(3)을 푸는 데 사용되는 방식으로 이어지기 때문이다.
# 한 번 구한 결과는 다시 구해지지 않는다.

# ---------------------------------------------------------------------------------------------------------------------
d = [0] * 100


def fibo(x):
    print('f(' + str(x) + ')', end=' ')
    if x in (1, 2):
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]


fibo(6)
