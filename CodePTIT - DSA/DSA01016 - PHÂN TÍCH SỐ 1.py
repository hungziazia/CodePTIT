def Try(limit, remain, a):
    if remain == 0:
        print(f"({' '.join(map(str, a))})", end=" ")
        return
    for i in range(limit, 0, -1):
        if remain >= i:
            Try(i, remain - i, a + [i])

for _ in range(int(input())):
    n = int(input())
    Try(n, n, [])
    print()