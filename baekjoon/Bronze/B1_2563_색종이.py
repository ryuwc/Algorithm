
arr = [[0]*100 for _ in range(100)]

N = int(input())
for n in range(N):
    c, r = map(int, input().split())
    for i in range(r, r+10):
        for j in range(c, c+10):
            arr[i][j] = 1

result = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 0:
            continue
        else:
            result += arr[i][j]

print(result)