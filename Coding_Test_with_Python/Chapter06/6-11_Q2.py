# 실전 문제 - 성적이 낮은 순서로 학생 출력하기(180p)

n = int(input())
data = []
for _ in range(n):
    input_data = input().split()
    data.append((input_data[0], input_data[1]))

data = sorted(data, key=lambda x: x[1])

for d in data:
    print(d[0], end=' ')
