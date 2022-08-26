import sys; sys.stdin = open('input_현주상자.txt', 'r')

for tc in range(int(input())):
    N, Q = map(int, input().split())
    boxes = [0]*N

    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            boxes[j] = i+1

    print(f'#{tc+1}', *boxes)