n = int(input())
colors = []
for _ in range(n):
    r, g, b = map(int, input().split())
    colors.append([r, g, b])

for i in range(1, n):
    colors[i][0] += min(colors[i - 1][1], colors[i - 1][2])
    colors[i][1] += min(colors[i - 1][2], colors[i - 1][0])
    colors[i][2] += min(colors[i - 1][0], colors[i - 1][1])

result = min(colors[n - 1][0], colors[n - 1][1], colors[n - 1][2])
print(result)