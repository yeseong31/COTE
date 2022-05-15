# 다이나믹 프로그래밍
# 어떤 문제는 메모리 공간을 약간 더 사용하면 연산 속도를 비약적으로 증가시킬 수 있는 방법이 있는데, 이를 '다이나믹 프로그래밍'이라 한다.

# 다이나믹 프로그래밍으로 해결할 수 있는 대표적인 예시로 '피보나치 수열'이 있다.
#     n번째 피보나치 수 = (n - 1)번째 피보나치 수 + (n - 2)번째 피보나치 수

# ---------------------------------------------------------------------------------------------------------------------
# 피보나치 함수(Fibonacci Function)를 재귀 함수로 구현
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)


print(fibo(4))

# 그런데 피보나치 수열의 소스코드를 이렇게 작성하면 심각한 문제가 생길 수 있다.
# f(n) 함수에서 n이 커지면 커질수록 수행 시간이 기하급수적으로 늘어나기 때문이다.
# 피보나치 수열의 시간 복잡도는 일반적으로 O(2^n)의 지수 시간이 소요된다.
# 즉 f(n)에서 n이 커지면 커질수록 반복해서 호출하는 수가 많아진다.
