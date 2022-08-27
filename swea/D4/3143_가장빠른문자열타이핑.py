import sys; sys.stdin = open('3143.txt', 'r')

for tc in range(int(input())):
    A, B = map(str, input().split())
    N, M = len(A), len(B)
    counts = 0
    i = 0
    while i < N:
        if A[i:i+M] == B:
            counts += 1
            i += len(B)
        else:
            i += 1
            counts += 1




    print(f'#{tc+1} {counts}')

