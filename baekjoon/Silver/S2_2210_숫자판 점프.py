import sys
sys.setrecursionlimit(1000000)

def dfs(depth, r, c, str):
    # depth가 5가 되면 return
    if depth == 5:
        rst.add(str)
        return
    for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nr, nc = r + di, c + dj
        if 0 <= nr < 5 and 0 <= nc < 5:
            # 방문 여부 상관 없이 무지성 dfs
            dfs(depth+1, nr, nc, str + arr[nr][nc])


arr = [list(map(str, input().split())) for _ in range(5)]

rst = set()
for i in range(5):
    for j in range(5):
        dfs(0, i, j, arr[i][j])

print(len(rst))