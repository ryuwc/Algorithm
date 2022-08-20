import sys; sys.stdin = open('input_삼성시버스.txt', 'r')


for tc in range(int(input())):
    N = int(input())
    ns = []
    for n in range(N):
        ns += [list(map(int, input().split()))]
    P = int(input())
    ps = []
    for p in range(P):
        ps += [int(input())]
    result = []
    for i in range(P):
        sums = 0
        for j in range(N):
            if ps[i] in range(ns[j][0], ns[j][1]+1):
                sums += 1
        result += [sums]
    print(f'#{tc+1}', *result)

