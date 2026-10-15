for _ in range(int(input())):
    s = input().strip()
    gray = [s[0]] + [str(int(s[i - 1]) ^ int(s[i])) for i in range(1, len(s))]
    print("".join(gray))