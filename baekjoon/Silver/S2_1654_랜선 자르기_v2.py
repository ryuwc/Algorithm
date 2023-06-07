import sys


def solve(start, end):
    # 탈출 조건
    if end - start <= 1:
        return start

    mid = (start + end) // 2
    num_cables = sum(item // mid for item in cables)

    if num_cables < N:
        return solve(start, mid)
    else:
        return solve(mid, end)


K, N = map(int, sys.stdin.readline().split())
cables = [int(sys.stdin.readline()) for _ in range(K)]
max_cable = max(cables)

print(solve(1, max_cable + 1))
