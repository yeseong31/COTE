from itertools import product

k, m = map(int, input().split())

N = [list(map(int, input().split()))[1:] for _ in range(k)]
print(max(map(lambda x: sum(i ** 2 for i in x) % m, product(*N))))
