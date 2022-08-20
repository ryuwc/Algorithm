import sys; sys.stdin = open('input_파리.txt', 'r')

for tc in range(int(input())):
    N, M = map(int, input().split())
    fly = []
    for f in range(N):
        fly += [list(map(int, input().split()))]

    result = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            sums = 0
            for k in range(i, i+M):
                for l in range(j, j+M):
                    sums += fly[k][l]
            if sums > result:
                result = sums
    print(f'#{tc+1}', result)