import sys; from collections import deque

'''
이 문제의 핵심은 bfs를 통해 치즈를 녹이는 것이다.
외부인 공기에서 bfs를 시작하여 치즈를 녹이는 것이다.
'''
def bfs(N, M):
    Q.append((0, 0))
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    total = 0
    while Q:
        r, c = Q.popleft()
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nr, nc = r + di, c + dj
            if 0 <= nr < N and 0 <= nc < M:
                if cheese[nr][nc] == 0 and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    Q.append((nr, nc))
                elif cheese[nr][nc] == 1:
                    cheese[nr][nc] = 0
                    total += 1
                    visited[nr][nc] = 1
    return total

N, M = map(int, sys.stdin.readline().split())
cheese = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
Q = deque()

cheese_lst = []     # 공기에 닿은 치즈의 갯수를 담을 리스트
cnt = 0             # 치즈가 모두 녹아 없어지는 시간
while True:
    cheese_lst.append(bfs(N, M))
    cnt += 1
    if sum(map(sum, cheese)) == 0:  # 남아있는 치즈가 없으면 break
        break




print(cnt)
print(cheese_lst[-1])
