import sys

sinput = sys.stdin.readline

T = int(sinput().rstrip())
for tc in range(T):
    n = int(sinput().rstrip())
    dp = [0] * 12
    dp[1], dp[2], dp[3] = 1, 2, 4
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    print(dp[n])