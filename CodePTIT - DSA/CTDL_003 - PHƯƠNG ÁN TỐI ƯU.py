n, m = map(int, input().split())
v = [0] + list(map(int, input().split()))
w = [0] + list(map(int, input().split()))

f = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        f[i][j] = max(f[i - 1][j], f[i - 1][j - w[i]] + v[i]) if j >= w[i] else f[i - 1][j]

print(f[n][m])
ans = []
j = m
for i in range(n, 0, -1):
    if f[i][j] != f[i - 1][j]:
        ans.append(1)
        j -= w[i]
    else:
        ans.append(0)
print(*ans[::-1])