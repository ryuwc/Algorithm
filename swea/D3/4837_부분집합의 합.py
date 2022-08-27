
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    counts = 0
    for i in range(1 << len(arr)):
        tmp = [arr[j] for j in range(len(arr)) if i&(1<<j)]
        sums = 0
        if len(tmp) == N:
            for k in tmp:
                sums += k
        if sums == K:
            counts += 1
    print(f'#{tc} {counts}')
