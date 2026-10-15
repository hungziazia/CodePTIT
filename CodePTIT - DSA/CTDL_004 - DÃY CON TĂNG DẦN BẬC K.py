from itertools import combinations

n, k = map(int, input().split())
a = list(map(int, input().split()))
c = 0

for j in combinations(a, k):
    if list(j) == sorted(j):
        c += 1

print(c)