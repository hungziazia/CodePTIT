from itertools import product

n = int(input())
for p in product((0, 1), repeat=n):
    if p == p[::-1]:
        print(*p)