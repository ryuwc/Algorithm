import sys

def solve(depth, N, M):
    # depth가 M과 같아질 때 리턴
    if depth == M:
        print(*ans)
        return
    for i in range(1, N+1):
        if visited[i]:
            continue
        if not ans:
            visited[i] = 1
            ans.append(i)
            solve(depth + 1, N, M)
            ans.pop()
            visited[i] = 0
        elif i > ans[-1]:
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


