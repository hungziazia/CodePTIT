for _ in range(int(input())):
    tc, s = input().split()
    s = list(s)
    i = len(s) - 2
    while i >= 0 and s[i] >= s[i + 1]: 
        i -= 1
    if i == -1:
        print(tc, "BIGGEST")
    else:
        j = len(s) - 1
        while s[j] <= s[i]: 
            j -= 1
        s[i], s[j] = s[j], s[i]
        s[i + 1:] = sorted(s[i + 1:])
        print(tc, "".join(s))