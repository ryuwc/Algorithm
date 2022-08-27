import sys; sys.stdin = open('input_농작물.txt', 'r')

for tc in range(int(input())):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    key = N//2

    all_sum = 0
    for i in range(N):
        for j in range(N):
            all_sum += farm[i][j]

    result = 0
    dr = [1]
    dc = [-1]
    for i in range(1):
        for j in range(key):
            for k in range(1):
                for l in range(key):
                    nr, nc = i + dr[k]*l, j + dc[k]*l
                    if nr < 0 or nr >= key or nc < 0 or nc >= key:
                        break
                    all_sum -= farm[nr][nc]
    dr = [1]
    dc = [1]
    for a in range(1):
        for b in range(key+1, N):
            for k in range(1):
                for l in range(key):
                    nr, nc = a + dr[k] * l, b + dc[k] * l
                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        break
                    all_sum -= farm[nr][nc]
    dr = [1]
    dc = [1]
    for a in range(key+1, N):
        for b in range(1):
            for k in range(1):
                for l in range(key):
                    nr, nc = a + dr[k] * l, b + dc[k] * l
                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        break
                    all_sum -= farm[nr][nc]
    dr = [1]
    dc = [-1]
    for a in range(key+1, N):
        for b in range(N-1, N):
            for k in range(1):
                for l in range(key):
                    nr, nc = a + dr[k] * l, b + dc[k] * l
                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        break
                    all_sum -= farm[nr][nc]

    print(f'#{tc+1}', all_sum)



