import sys

def dfs(N, r, c):           # dfs탐색
    visited[r][c] = 1       # 일단, visited에 방문 표시
    global total
    total += 1              # dfs가 실행 된다는 것은 주변에 아파트가 있다는 것, 아파트 수를 더해줌
    for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:   # 상,하,좌,우로 델타주기
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N:                         # 일단, nr, nc의 경계 체크
            if maps[nr][nc] == 1 and visited[nr][nc] == 0:      # 아파트가 있고, 방문하지 않은 경우에만
                dfs(N, nr, nc)                                  # dfs 재귀

N = int(sys.stdin.readline())
maps = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]

total = 0       # 아파트 수
nums = []       # 각 단지의 아파트 수를 담을 리스트
for i in range(N):
    for j in range(N):
        if maps[i][j] == 1 and visited[i][j] == 0:  # 아파트가 있고, 방문 하지 않았다면, dfs를 돌려준다.
            dfs(N, i, j)
            nums.append(total)      # 아파트 수를 넣어주고
            total = 0               # 0으로 초기화

nums.sort()
print(len(nums))
for i in nums:
    print(i)
