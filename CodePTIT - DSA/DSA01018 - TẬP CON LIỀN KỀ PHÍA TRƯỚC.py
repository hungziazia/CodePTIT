for _ in range(int(input())):
    n, k = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    i = k
    while i > 0 and a[i] == a[i - 1] + 1:
        i -= 1
    if i > 0:
        a[i] -= 1
    for j in range(i + 1, k + 1):
        a[j] = n - k + j
    print(*a[1:])