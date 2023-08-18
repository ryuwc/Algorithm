import sys

sinput = sys.stdin.readline
print = sys.stdout.write

T = int(sinput())
for tc in range(T):
    N = int(sinput().rstrip())

    dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * (N - 9)
    for i in range(10, N):
        dp[i] = dp[i-2] + dp[i-3]

    print(f'{dp[N-1]}\n')
