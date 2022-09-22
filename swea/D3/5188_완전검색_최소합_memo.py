import sys; sys.stdin = open('sample_input_최소합.txt', 'r')


def dfs(r, c, s):
    global result, cnt
    if s > result:
        return
    if r == N-1 and c == N-1:
        result = min(result, s)
        return
    for di, dj in [[1, 0], [0, 1]]:
        nr, nc = r + di, c + dj
        if 0 <= nr < N and 0 <= nc < N:
            dfs(nr, nc, s+arr[nr][nc])

def dfs2(r, c):
    if r == 0 and c == 0:
        return arr[0][0]
    if memo[r][c] != -1:
        return memo[r][c]
    else:
        left = up = 0xfffff
        if c - 1 >= 0:
            left = dfs2(r, c-1)
        if r - 1 >= 0:
            up = dfs2(r-1, c)
        memo[r][c] = min(left, up) + arr[r][c]
        return memo[r][c]

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0xffffffff
    # dfs(0, 0, arr[0][0])
    # print(dfs2(0, 0))
    # print(f'#{tc+1}', result)
    memo = [[0]*N for _ in range(N)]
    memo[0][0] = arr[0][0]
    # 메모의 초기값을 0으로 하면 안됨. 0이라는 값이 실제로 존재할 수 있기 때문.
    for i in range(1, N):
        memo[0][i] = memo[0][i-1] + arr[0][i]
        memo[i][0] = memo[i-1][0] + arr[i][0]

    for i in range(1, N):
        for j in range(1, N):
            memo[i][j] = min(memo[i-1][j], memo[i][j-1]) + arr[i][j]

    print(f'#{tc+1}', memo[N-1][N-1])

for i in range(N):
    print(*arr[i], '|', *memo[i])
