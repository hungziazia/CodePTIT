for _ in range(int(input())):
    s = list(input().strip())
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '1': 
            s[i] = '0'
        else:
            s[i] = '1'
            break
    print("".join(s))