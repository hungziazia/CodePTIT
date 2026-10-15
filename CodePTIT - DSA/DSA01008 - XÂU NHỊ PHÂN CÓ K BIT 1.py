from itertools import product

for _ in range(int(input())):
    n, k = map(int, input().split())
    for p in product((0, 1), repeat=n):
        if sum(p) == k:
            print("".join(map(str, p)))