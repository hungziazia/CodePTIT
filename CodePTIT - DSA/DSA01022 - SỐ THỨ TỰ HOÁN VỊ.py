from itertools import permutations

for _ in range(int(input())):
    n = int(input())
    a = tuple(map(int, input().split()))
    for i, p in enumerate(permutations(range(1, n + 1)), 1):
        if p == a:
            print(i)
            break