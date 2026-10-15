n = int(input())
a = list(map(int, input().split()))
x = int(input())
print(*(i for i in a if i != x))