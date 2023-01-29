import sys; import heapq

arr = []
N = int(sys.stdin.readline())
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

S = []
rst = 0
for i in range(N):
    while S and S[-1] <= arr[i]:
        S.pop()
    S.append(arr[i])
    # print(S)
    rst += len(S) -1

print(rst)
