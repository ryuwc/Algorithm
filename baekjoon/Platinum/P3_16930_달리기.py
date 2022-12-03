import sys; from collections import deque

def solve(sr, sc, er, ec):
    Q = deque()
    Q.append((sr, sc))

    # 거리 저장할 배열
    dist = [[-1] * M for _ in range(N)]
    # 출발점 0으로 초기화
    dist[sr][sc] = 0
    while Q:
        r, c = Q.popleft()
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            for i in range(1, L + 1):
                nr, nc = r + (di * i), c + (dj * i)
                # 도착점에서 return
                if nr == er and nc == ec:
                   return dist[r][c] + 1
                # 경계를 벗어나거나, 벽이면 갈 수 없으니 break
                if not (0 <= nr < N and 0 <= nc < M) or arr[nr][nc] == '#':
                    break
                # nr, nc 좌표의 dist가 -1이 아니면서 현재 r, c의 거리보다 작으면 갈 필요가 없으니 break
                if dist[nr][nc] != -1 and dist[nr][nc] <= dist[r][c]:
                    break
                if dist[nr][nc] == -1:
                    Q.append((nr, nc))
                    dist[nr][nc] = dist[r][c] + 1
    return -1

N, M, L = map(int, sys.stdin.readline().strip().split())

arr = [list(sys.stdin.readline().strip()) for _ in range(N)]

sr, sc, er, ec = map(int, sys.stdin.readline().strip().split())

sr -= 1; sc -= 1; er -=1; ec -= 1

# for line in dist:
#     print(line)
#
# for line in visited:
#     print(line)

print(solve(sr, sc, er, ec))
