
T = int(input())

for _ in range(1, T + 1):
    N = int(input())
    card = list(map(int, list(input())))
    counts = [0] * 10
    for i in card:
        counts[i] += 1
    multi = 0
    multi_idx = 0
    for i in range(len(counts)):
        if multi <= counts[i]:
            multi = counts[i]
            multi_idx = i

    print(f'#{_} {multi_idx} {multi}')


    # print(f'#{_} {card[-1] - card[0]}')


