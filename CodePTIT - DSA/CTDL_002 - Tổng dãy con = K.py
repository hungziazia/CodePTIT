from itertools import product

n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0

for p in product((0, 1), repeat=n):
    sub = [a[i] for i in range(n) if p[i] == 1]
    if sum(sub) == k:
        print(*sub)
        cnt += 1

print(cnt)