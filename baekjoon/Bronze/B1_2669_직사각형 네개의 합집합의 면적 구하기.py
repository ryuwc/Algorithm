
arr= [[0]*100 for _ in range(100)]

for t in range(4):
    c1, r1, c2, r2 = map(int, input().split())
    for i in range(r1, r2):
        for j in range(c1, c2):
            arr[i][j] = 1

result = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 0:
            continue
        else:
            result += arr[i][j]
print(result)