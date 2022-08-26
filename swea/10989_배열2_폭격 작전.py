import sys; sys.stdin = open('input_폭격.txt', 'r')

for tc in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    result = 0
    for m in range(M):
        r, c, length = map(int, input().split())
        for k in range(4):
            for l in range(length+1):
                nr, nc = r + dr[k]*l, c + dc[k]*l
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    break
                else:
                    result += arr[nr][nc]
                    arr[nr][nc] = 0
    print(f'#{tc+1}', result)

