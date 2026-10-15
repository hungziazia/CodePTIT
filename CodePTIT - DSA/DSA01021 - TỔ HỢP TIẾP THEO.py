for _ in range(int(input())):
    n, k = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    old_set = set(a[1:])
    
    i = k
    while i > 0 and a[i] == n - k + i:
        i -= 1
        
    if i == 0:
        print(k)
    else:
        a[i] += 1
        for j in range(i + 1, k + 1):
            a[j] = a[j - 1] + 1
        print(sum(1 for x in a[1:] if x not in old_set))