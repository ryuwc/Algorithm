
T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    counts_A = 0
    counts_B = 0

    l = 1
    r = len(range(P))
    c = P // 2
    while l <= r:
        counts_A += 1
        if c < A:
            l = c
        elif c > A:
            r = c
        else:
            break
        c = (l + r) // 2

    l = 1
    r = len(range(P))
    c = P // 2
    while l <= r:
        counts_B += 1
        if c < B:
            l = c
        elif c > B:
            r = c
        else:
            break
        c = (l + r) // 2

    if counts_A == counts_B:
        print(f'#{tc} 0')
    elif counts_A > counts_B:
        print(f'#{tc} B')
    elif counts_A < counts_B:
        print(f'#{tc} A')