from itertools import permutations

n = int(input())
a = sorted(map(int, input().split()))
for p in permutations(a):
    print(*p)