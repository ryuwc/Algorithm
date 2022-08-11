
T = int(input())

for _ in range(1, T + 1):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    max_sum = 0
    min_sum = 9999999999999999999999999999999999999999999
    for i in range(0, N-M+1):
        summary = 0
        for j in range(M):
            summary += num[i+j]
        if summary > max_sum:
            max_sum = summary
        summary = 0
        for j in range(M):
            summary += num[i+j]
        if summary < min_sum:
            min_sum = summary
    print(f'#{_} {max_sum - min_sum}')


# 14067 15465 17380 16859 9724 11603 15457 16753
