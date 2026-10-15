from itertools import combinations

for _ in range(int(input())):
    n, k = map(int, input().split())
    for c in combinations(range(1, n + 1), k):
        print("".join(map(str, c)), end=" ")
    print()