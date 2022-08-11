
T = int(input())

for _ in range(1, T + 1):
    K, N, M = map(int, input().split())
    num = list(map(int, input().split()))
    counts = 0
    bus = 0
    minus = 0
    for i in range(0, len(num) - 1):
        if num[i + 1] - num[i] > K:
            minus += 1
            break
    if minus > 0:
        print(f'#{_} 0')
    else:
        while bus <= N:
            bus += K
            while bus <= N:
                if bus == N:
                    break
                elif bus not in num and bus <= N:
                    bus -= 1
                else:
                    counts += 1
                    break
        else:
            print(f'#{_} {counts}')