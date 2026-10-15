n = int(input())
a = list(map(int, input().split()))
print(*list(dict.fromkeys(a)))