for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    old_set = set(a)
    i = k - 1
    while i >= 0 and a[i] == n - k + i + 1:
        i -= 1
    if i < 0:
        print(k)
    else:
        a[i] += 1
        for j in range(i + 1, k):
            a[j] = a[j - 1] + 1
        print(len(set(a) - old_set))