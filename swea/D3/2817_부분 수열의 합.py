
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))

    counts = 0
    for i in range(1<<N):
        summary = 0
        for j in range(N):
            if i & (1<<j):
                summary += numbers[j]
        if summary == K:
            counts += 1
    print(f'#{tc} {counts}')


