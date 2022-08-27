import sys; sys.stdin = open('4861.txt', 'r')

for tc in range(int(input())):
    N, M = map(int, input().split())
    strs = [input() for _ in range(N)]
    result = ''
    for i in range(N):
        for j in range(N-M+1):
            tmp1 = ''
            tmp2 = ''
            for k in range(j, j+M):
                tmp1 += strs[i][k]
            for k in range(M-1+j, j-1, -1):
                tmp2 += strs[i][k]
            if tmp1 == tmp2:
                result = tmp1
    if len(result) < 1:
        for j in range(N):
            for i in range(N - M + 1):
                tmp1 = ''
                tmp2 = ''
                for k in range(i, i + M):
                    tmp1 += strs[k][j]
                for k in range(M - 1 + i, i - 1, -1):
                    tmp2 += strs[k][j]
                if tmp1 == tmp2:
                    result = tmp1

    print(f'#{tc+1} {result}')
