from itertools import product

n = int(input())
for p in product("68", repeat=n):
    s = "".join(p)
    if s[0] == '8' and s[-1] == '6' and "88" not in s and "6666" not in s:
        print(s)