import sys

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

for i in range(1, N):
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]
    arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1]
    arr[i][2] = min(arr[i-1][1], arr[i-1][0]) + arr[i][2]

rst = 9e9
for j in range(3):
    rst = min(rst, arr[N-1][j])

print(rst)
