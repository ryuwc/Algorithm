
N = int(input())
road = list(map(int, input().split()))

road.append(0)
result = 0
tmp = []
for i in range(N):
    now_road = road[i]
    next_road = road[i+1]
    if now_road < next_road:
        tmp.append(now_road)
        tmp.append(next_road)
    elif i == N-1 and tmp:
        result = max(result, tmp[-1] - tmp[0])
        tmp.clear()
    else:
        if tmp:
            result = max(result, tmp[-1] - tmp[0])
            tmp.clear()

print(result)


