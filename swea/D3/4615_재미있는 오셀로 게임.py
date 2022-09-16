import sys; sys.stdin = open('input_오셀로.txt', 'r')

for tc in range(int(input())):
    N, M = map(int, input().split())
    osero = [[0] * N for _ in range(N)]
    osero[N//2][N//2] = 2
    osero[N//2-1][N//2-1] = 2
    osero[N//2-1][N//2] = 1
    osero[N//2][N//2-1] = 1

    # 현재 위치 주변 8방향 설정
    dr = [1, 0, -1, 0, -1, -1, 1, 1]
    dc = [0, 1, 0, -1, 1, -1, 1, -1]
    for _ in range(M):
        c, r, bw = map(int, input().split())
        r -= 1
        c -= 1
        osero[r][c] = bw            # 일단, 이 위치에 돌을 넣어줌
        for i in range(8):          # 8방향 탐색 시작
           for l in range(1, N):    # 많이 가봐야 N만큼 간다.
               nr, nc = r + dr[i] * l, c + dc[i] * l
               if 0 <= nr < N and 0 <= nc < N:
                   # 현재 위치의 델타가 내 돌이 아니고, 0이 아닌경우 (상대 돌이 있는 경우)
                   # 쭉 가면서 l이 증가한다.
                   if osero[nr][nc] != bw and osero[nr][nc] != 0:
                       continue
                   # 그러다가 내 돌이 나타날 것이다.
                   elif osero[nr][nc] == bw:
                          # 그럼 그 사이를 내 돌로 바꿔준다.
                          for k in range(1, l):
                            osero[r + dr[i] * k][c + dc[i] * k] = bw
                          # 다 바꿧으면, 방향을 바꾼다.
                          break

    result =[0, 0]
    for i in range(N):
        for j in range(N):
            if osero[i][j] == 1:
                result[0] += 1
            elif osero[i][j] == 2:
                result[1] += 1

    print(f'#{tc+1}', *result)
