import sys

def solve(depth, N, M):
    if depth == M:
        print(*ans)
        return
    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = 1
        ans.append(i)
        solve(depth+1, N, M)

        ans.pop()
        visited[i] = 0

N, M = map(int, sys.stdin.readline().split())
arr = []
for i in range(1, N+1):
    arr.append(i)

visited = [0] * (N+1)
ans = []
solve(0, N, M)


