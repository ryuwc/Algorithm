
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    counts = 0
    arr = [[0] * 10 for _ in range(10)]
    for i in range(N):
        c0, r0, c1, r1, type_color = map(int, input().split())
        lst = [c0, r0, c1, r1, type_color]

        for j in range(r0, r1+1):
            for k in range(c0, c1+1):
                if arr[j][k] == 0 or arr[j][k] == type_color:
                    arr[j][k] = type_color
                else:
                    arr[j][k] = -1

    for i in range(10):
        for j in range(10):
            if arr[i][j] == -1:
                counts += 1
    print(f'#{tc} {counts}')
    # for line in arr:
    #     print(*line)
