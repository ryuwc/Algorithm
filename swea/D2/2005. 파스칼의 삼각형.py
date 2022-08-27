# import sys; sys.stdin = open('2005.txt', 'r')

# 초기값 설정에 주의
memo = [[0] * 100 for _ in range(100)]
def comb(n, r):
    if r == 0 or n == r:
        memo[n][r] = 1
        return 1
    # (n, r) 의 문제를 이미 풀었나 확인?
    # 이이 해결한 문제라면 답을 읽어서 반환
    if memo[n][r]:
        return memo[n][r]

    # 그렇지 않다면, 문제를 풀어서 답을 저장하고 반환
    memo[n][r] = comb(n - 1, r - 1) + comb(n - 1, r)
    return memo[n][r]
print(comb(10, 5))
# ================================================
N = 10
memo = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(0, i + 1):
        if j == 0 or i == j:
            memo[i][j] = 1
        else:
            memo[i][j] = memo[i - 1][j - 1] + memo[i - 1][j]

for i in range(N):
    for j in range(0, i + 1):
        print(f'{memo[i][j]:3}', end=' ')
    print()


