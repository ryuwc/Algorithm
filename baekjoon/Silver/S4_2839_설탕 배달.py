def solve(N):
    cnt = N // 5
    N = N % 5
    while cnt >= 0:
        if N % 3 == 0:
            cnt += N // 3
            return print(cnt)
        N += 5
        cnt -= 1
    print(-1)


N = int(input())

solve(N)
