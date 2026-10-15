MOD = 10**9 + 7

for _ in range(int(input())):
    n, k = map(int, input().split())
    print(pow(n, k, MOD))