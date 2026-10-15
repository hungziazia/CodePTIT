for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    i = n - 2
    while i >= 0 and a[i] >= a[i + 1]: 
        i -= 1
    if i < 0: 
        a.sort()
    else:
        j = n - 1
        while a[j] <= a[i]: 
            j -= 1
        a[i], a[j] = a[j], a[i]
        a[i + 1:] = reversed(a[i + 1:])
    print(*a)