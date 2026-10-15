from itertools import permutations

for _ in range(int(input())):
    n = int(input())
    for p in permutations(range(1, n + 1)):
        print("".join(map(str, p)), end=" ")
    print()