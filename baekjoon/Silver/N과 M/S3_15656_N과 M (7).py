import sys

def solve(depth, N, M):
    if depth==M:
        print(*ans)
        return
    for i in arr:
        ans.append(i)
        solve(depth+1, N, M)
        ans.pop()





N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
max_arr = max(arr)
visited = [0] * (max_arr+1)
ans = []

solve(0, N, M)