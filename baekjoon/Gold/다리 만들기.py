import sys; from collections import deque;
# sys.stdin = open('다리.txt', 'r')
sys.setrecursionlimit(10**6)


def bfs(r, c):
    my_color = map[r][c]
    Q = deque()
    Q.append((r, c))
    visit2[r][c] = 1
    while Q:
        r, c = Q.popleft()
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nr, nc = r + di, c + dj
            if 0 <= nr < N and 0 <= nc < N:
                # 섬 주변이 0이면 visit에 거리를 넣어주고 큐에 저장
                if map[nr][nc] == 0 and not visit[nr][nc]:
                    visit[nr][nc] = visit[r][c] + 1
                    Q.append((nr, nc))
                # 같은 섬이고 방문하지 않았다면 방문표시 하고 큐에 저장
                elif map[nr][nc] == my_color and not visit2[nr][nc]:
                    visit2[nr][nc] = 1
                    Q.append((nr, nc))
                # 그러다가 다른 섬을 만나면 그 위치의 거리 값을 return하고 함수 종료
                elif map[nr][nc] != my_color and map[nr][nc] != 0:
                    return visit[r][c]

# 각 섬들을 구분하기 위해 섬에 번호를 입혀줄 함수
def chang_color(r, c):
    tmp_visit[r][c] = 1
    map[r][c] = now_color
    for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nr, nc = r + di, c + dj
        if 0 <= nr < N and 0 <= nc < N:
            if not tmp_visit[nr][nc] and map[nr][nc] == 1:
                chang_color(nr, nc)




N = int(sys.stdin.readline())

map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


# 각 섬들에 대해 번호를 바꿔줌 1번 섬, 2번섬 .....
tmp_visit = [[0]*N for _ in range(N)]
now_color = 1
for i in range(N):
    for j in range(N):
        if map[i][j] == 1 and tmp_visit[i][j] == 0:
            chang_color(i, j)
            now_color += 1


result = 1e9
for i in range(N):
    for j in range(N):
        # 섬이고
        if map[i][j]:
            # 위아래가 0이 아니면 후보에서 탈락
            if 0 <= i+1 < N and 0 <= i-1 < N:
                if map[i+1][j] > 0 and map[i-1][j] > 0:
                    continue
            # 좌우도 마찬가지
            if 0 <= j + 1 < N and 0 <= j - 1 < N:
                if map[i][j+1] > 0 and map[i][j-1] > 0:
                    continue
            # visit은 섬의 주변 0들에 대해 거리를 저장
            # visit2는 섬일 때 방문 표시 위해 만듬
            visit = [[0] * N for _ in range(N)]
            visit2 = [[0] * N for _ in range(N)]
            result = min(bfs(i, j), result)

print(result)
