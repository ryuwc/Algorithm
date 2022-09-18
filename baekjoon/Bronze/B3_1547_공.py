

M = int(input())
result = 1
for m in range(M):
    a, b = map(int, input().split())
    if a == result:
        result = b
    elif b == result:
        result = a
print(result)