from itertools import combinations

while True:
    n, k, s = map(int, input().split())
    if n == 0 and k == 0 and s == 0: 
        break
    print(sum(1 for c in combinations(range(1, n + 1), k) if sum(c) == s))