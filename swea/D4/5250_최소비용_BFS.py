import sys; sys.stdin = open('5250.txt', 'r')
from collections import deque

def bfs(r, c):
    # 0, 0의 visited의 값은 0으로 초기화
    visited[r][c] = 0
    Q = deque()
    Q.append((r, c))
    while Q:
        r, c = Q.popleft()
        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                # Q와 visited에 넣어 줄지 말지 판단의 값을 넣어줄 변수
                val = 0
                # 만약 다음 칸이 지금 칸보다 크면 val에 그 차이를 저장
                if arr[nr][nc] > arr[r][c]:
                    val = arr[nr][nc] - arr[r][c]

                # 만약 다음 칸의 visited가
                # 현재 칸의 수 + 1(다음 칸으로 가려면 1더해주고 가야됨) + 두 칸의 차이보다 작다면, visited에 거리 저장, Q에 추가
                if visited[r][c] + 1 + val < visited[nr][nc]:
                    visited[nr][nc] = visited[r][c] + 1 + val
                    Q.append((nr, nc))

    return visited[N-1][N-1]

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # visited는 거리를 저장할 변수임, 일단 큰 값으로 초기화 해줌
    visited = [[1e9] * N for _ in range(N)]
    bfs(0, 0)
    print(f'#{tc+1}', visited[N-1][N-1])

