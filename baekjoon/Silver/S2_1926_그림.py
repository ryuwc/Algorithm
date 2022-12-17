import sys; from collections import deque


def bfs(r, c, visit):
    Q = deque()
    Q.append((r, c))
    visit.add((r, c))
    tmp_rst = 1
    while Q:
        r, c = Q.popleft()
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nr, nc = r + di, c + dj
            # 범위 체크, 방문 체크, 1인지 체크
            if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in visit and arr[nr][nc] == 1:
                visit.add((nr, nc))
                tmp_rst += 1
                Q.append((nr, nc))
    
    return tmp_rst  # 현재 그림의 영역을 리턴


def main():
    rst = 0
    cnt = 0
    visit = set()
    for i in range(N):
        for j in range(M):
            # 방문하지 않았고, 1이면 bfs탐색
            if (i, j) not in visit and arr[i][j] == 1:
                # bfs함수는 그림의 영역을 리턴하므로 rst갱신
                rst = max(rst, bfs(i, j, visit))
                cnt += 1

    print(cnt)
    print(rst)


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

    main()
