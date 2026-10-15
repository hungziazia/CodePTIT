for _ in range(int(input())):
    n, k = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    i = k
    while i > 0 and a[i] == n - k + i: 
        i -= 1
    if i == 0: 
        a[1:] = range(1, k + 1)
    else:
        a[i] += 1
        for j in range(i + 1, k + 1): 
            a[j] = a[j - 1] + 1
    print(*a[1:])