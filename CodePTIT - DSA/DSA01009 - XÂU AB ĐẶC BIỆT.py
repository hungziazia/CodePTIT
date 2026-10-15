from itertools import product

n, k = map(int, input().split())
z = 'A' * k
res = ["".join(p) for p in product("AB", repeat=n) if "".join(p).split('B').count(z) == 1]
print(len(res))
for i in res:
    print(i)