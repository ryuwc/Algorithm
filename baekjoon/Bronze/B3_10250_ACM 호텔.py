T = int(input())
for tc in range(T):
    H, W, N = map(int, input().split())

    if N % H == 0:
        height = H
        width = N // H
    else:
        height = N % H
        width = N // H + 1

    print(f'{height * 100 + width}')
