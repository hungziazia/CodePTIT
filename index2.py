from itertools import product
n = int(input())
a=[]
for i in product(['0', '1'], repeat=n):
    s = " ".join(i)
    a.append(s)
for i in a:
    if i == i[::-1]:
        print(i)