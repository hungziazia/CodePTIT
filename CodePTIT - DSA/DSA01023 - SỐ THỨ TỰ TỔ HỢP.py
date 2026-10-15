from itertools import combinations

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = tuple(map(int, input().split()))
    for i, c in enumerate(combinations(range(1, n + 1), k), 1):
        if c == a:
            print(i)
            break