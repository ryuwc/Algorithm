from collections import deque
import sys
from heapq import heappush, heappop
# sys.stdin = open('아기상어.txt', 'r')

def find_shark():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                return i, j

def solve():
    global size, eat, rst, visit, target
    Q = deque()
    # 일단 현재 상어 위치 찾아서 Q에 넣어주고, 상어가 있는 좌표를 방문 처리
    sr, sc = find_shark()
    Q.append((sr, sc))
    visit = [[0] * N for _ in range(N)]
    visit[sr][sc] = 1

    # 먹을 물고기들 넣어줄 리스트, [[거리, r, c], ...] 이렇게 들어갈 것임
    target = []
    while Q:
        r, c = Q.popleft()
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nr, nc = r+di, c+dj
            if 0 <= nr < N and 0 <= nc < N and visit[nr][nc] == 0:
                if arr[nr][nc] <= size:
                    # 일단 움직일 수 있는 곳에 거리를 visit에 적어주고, Q에 추가
                    visit[nr][nc] = visit[r][c] + 1
                    Q.append((nr, nc))
                    # 그 중에 먹을수 있는 물고기는 target에 heappush
                    if 0 < arr[nr][nc] < size:
                        heappush(target, (visit[r][c], nr, nc))

    # target이 존재한다면, 0번째 인덱스가 가장 거리가 가까운 물고기의 위치임(힙큐를 사용해서), 행, 열은 순서대로 넣었으니까 아마 알아서 정렬되었을 것임
    if target:
        return target[0][0], target[0][1], target[0][2], sr, sc
    else:
        return False

N = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
size = 2
eat = 0

rst = 0
while True:
    target = solve()
    if target:
        # 거리==시간, target물고기 행, 열, 상어 위치 행, 열
        time, tr, tc, sr, sc = target[0], target[1], target[2], target[3], target[4]
        rst += time
        arr[tr][tc] = 9
        arr[sr][sc] = 0
        eat += 1
        if eat >= size:
            size += 1
            eat = 0
    else:
        break

print(rst)
