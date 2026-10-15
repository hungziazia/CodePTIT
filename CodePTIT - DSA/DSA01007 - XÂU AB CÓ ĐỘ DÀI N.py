from itertools import product

for _ in range(int(input())):
    n = int(input())
    for p in product("AB", repeat=n):
        print("".join(p), end=" ")
    print()