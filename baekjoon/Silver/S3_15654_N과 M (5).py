import sys

def solve(depth, N, M):
    if depth == M:
        print(*ans)
        return
    for i in arr:
        if visited[i]:
            continue
        visited[i] = 1
        ans.append(i)
        solve(depth+1, N, M)
        # return후 할 작업
        ans.pop()
        visited[i] = 0



N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
max_arr = max(arr)
visited = [0] * (max_arr+1)
ans = []

solve(0, N, M)