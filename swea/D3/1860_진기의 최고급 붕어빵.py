import sys; sys.stdin = open('input_붕어빵.txt', 'r')

for tc in range(int(input())):
    N, M, K = map(int, input().split())
    come = list(map(int, input().split()))

    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if come[j] > come[j+1]:
                come[j], come[j+1] = come[j+1], come[j]

    for i in range(N):
        bread = (come[i] // M) * K
        if bread < i + 1:
            print(f'#{tc+1}', 'Impossible')
            break
    else:
        print(f'#{tc+1}', 'Possible')

