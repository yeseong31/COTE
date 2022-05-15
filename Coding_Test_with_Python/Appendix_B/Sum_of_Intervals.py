# 구간 합 계산
# 연속적으로 나열된 N개의 수가 있을 때, 특정 구간의 모든 수를 합한 값을 구하는 문제

# 이러한 문제는 여러 개의 쿼리(Query)로 구성되는 문제 형태로 출제되는 경우가 많다.
# 예를 들어 M개의 쿼리가 존재한다고 가정해보자.
# 각 쿼리는 Left와 Right로 구성되며, 이는 [Left, Right]의 구간을 의미한다.

# 만약 M개의 쿼리 각각, 매번 구간 합을 계산한다면 이 알고리즘의 시간 복잡도는 O(NM)으로 매우 비효율적이다.
# 알고리즘을 설계할 때 고려해야 할 점은, 여러 번 사용될 만한 정보는 미리 구하여 저장해 놓는 것이 유리하다는 것이다.
# 구간 합 계산을 위해 가장 많이 사용되는 기법이 바로 '접두사 합(Prefix Sum)'이다.
# 이때 접두사 합이란 리스트의 맨 앞부터 특정 위치까지의 합을 구해 놓은 것이다.

# (1) N개의 수에 대하여 접두사 합을 계산하여 배열 P에 저장한다.
# (2) 매 M개의 퉈리 정보 [L, R]을 확인할 때, 구간 합은 P[R] - P[L - 1]이다.

# 매 쿼리가 들어왔을 때, P[R] - P[L - 1]을 계산하면 바로 구간 합을 구할 수 있다.
# 따라서 매 쿼리당 계산 시간은 O(1)이 되고, 전체 구간 합을 모두 계산하는 작업은 O(N + M)이 된다.

# 데이터의 수 N과 전체 데이터 선언
n = 5
data = [10, 20, 30, 40, 50]

# 접두사 합 배열 계산
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

# 구간 합 계산
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])
