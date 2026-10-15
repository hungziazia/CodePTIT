for _ in range(int(input())):
    s = input().strip()
    bin_str = [s[0]]
    for i in range(1, len(s)):
        bin_str.append(str(int(bin_str[-1]) ^ int(s[i])))
    print("".join(bin_str))