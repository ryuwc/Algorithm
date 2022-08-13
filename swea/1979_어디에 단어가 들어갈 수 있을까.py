# import sys; sys.stdin = open('input_어디.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    counts_r = 0
    counts_c = 0
    for i in range(N):
        cts = 0
        for j in range(N):
            if j == N-1 and arr[i][j] == 1:
                cts += 1
                if cts == K:
                    counts_r += 1
            elif arr[i][j] == 1:
                cts += 1
            elif arr[i][j] == 0 and cts ==K:
                counts_r += 1
                cts = 0
            else:
                cts = 0
    for j in range(N):
        cts = 0
        for i in range(N):
            if i == N - 1 and arr[i][j] == 1:
                cts += 1
                if cts == K:
                    counts_c += 1
            elif arr[i][j] == 1:
                cts += 1
            elif arr[i][j] == 0 and cts == K:
                counts_c += 1
                cts = 0
            else:
                cts = 0
    print(f'#{tc} {counts_r+counts_c}')