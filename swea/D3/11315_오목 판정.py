import sys; sys.stdin = open('input_오목.txt', 'r')

def find_omok(N):
    for i in range(N):
        for j in range(N):
            for k in range(4):
                oh = 0
                for l in range(5):
                    nr, nc = i + dr[k] * l, j + dc[k] * l
                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        break
                    else:
                        if omok[nr][nc] == 'o':
                            oh += 1
                if oh == 5:
                    return 'YES'
    return 'NO'

for tc in range(int(input())):
    N = int(input())
    omok = [list(input()) for _ in range(N)]

    dr = [0, 1, 1, 1]      # 우, 하, 좌우대각, 우좌대각
    dc = [1, 0, 1, -1]

    print(f'#{tc+1}', find_omok(N))


