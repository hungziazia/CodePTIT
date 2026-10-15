for _ in range(int(input())):
    s = list(input().strip())
    i = len(s) - 1
    while i >= 0 and s[i] == '0':
        s[i] = '1'
        i -= 1
    if i >= 0:
        s[i] = '0'
    print("".join(s))