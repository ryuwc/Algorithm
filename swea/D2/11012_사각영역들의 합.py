import sys; sys.stdin = open('input_사각영역.txt', 'r')

for tc in range(int(input())):
    N, M = map(int, input().split())
    N_array = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for m in range(M):
        r, c, length = map(int, input().split())
        for i in range(r, r+length):
            for j in range(c, c+length):
                if 0 <= j < N and 0 <= i < N:
                    result += N_array[i][j]
                    N_array[i][j] = 0
                else:
                    break
    print(f'#{tc+1}', result)
