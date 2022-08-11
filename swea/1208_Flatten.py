
for _ in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))
    N = len(box)



    for j in range(dump):
        max_height = box[0]
        min_height = box[0]
        for i in range(N):
            if box[i] > max_height:
                max_height = box[i]
            elif box[i] < min_height:
                min_height = box[i]
        idx_max_height = 0
        idx_mim_height = 0
        idx = -1
        for i in box:
            idx += 1
            if i == max_height:
                idx_max_height = idx
            elif i == min_height:
                idx_min_height = idx
        box[idx_max_height] -= 1
        box[idx_min_height] += 1
        mini = box[idx_max_height]
        for i in range(N):
            if box[i] < mini:
                mini = box[i]

    print(f'#{_} {max_height - mini}')

