# DSA01019 - HAHAHA
from itertools import product

for _ in range(int(input())):
    n = int(input())
    for p in product("AH", repeat=n):
        s = "".join(p)
        if s[0] == 'H' and s[-1] == 'A' and "HH" not in s:
            print(s)