from itertools import permutations

for _ in range(int(input())):
    n = int(input())
    for p in sorted(permutations(range(1, n + 1)), reverse=True):
        print("".join(map(str, p)), end=" ")
    print()