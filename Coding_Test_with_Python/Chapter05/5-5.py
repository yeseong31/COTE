# 2가지 방식으로 구현한 팩토리얼 예제
def factorial_iterative(n):
    result = 1
    # 1부터 n까지 수를 차례대로 곱하기
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


# 각각의 방식으로 구현한 n! 출력
print('반복적으로 구현: ', factorial_iterative(5))
print('재귀적으로 구현: ', factorial_recursive(5))

# 수학에서 점화식은 특정한 함수를 자신보다 더 작은 변수에 대한 함수와의 관계로 표현한 것.
# 이 개념은 이후 8장의 '다이나믹 프로그래밍'으로 이어지므로 매우 중요함.
