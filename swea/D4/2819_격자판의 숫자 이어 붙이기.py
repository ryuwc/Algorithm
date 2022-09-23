import sys; sys.stdin = open('input_숫자이어붙이기.txt', 'r')
sys.setrecursionlimit(1000000)

def dfs(depth, r, c, str):
    if depth == 6:
        result.add(str)
        return
    for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nr, nc = r + di, c + dj
        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(depth+1, nr, nc, str + arr[nr][nc])
for tc in range(int(input())):
    arr = [list(map(str, input().split())) for _ in range(4)]

    result = set()
    for i in range(4):
        for j in range(4):
            dfs(0, i, j, arr[i][j])
    print(f'#{tc+1}', len(result))
