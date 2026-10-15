for _ in range(int(input())):
    n = int(input())
    for i in range(1 << n):
        print(f"{i ^ (i >> 1):0{n}b}", end=" ")
    print()