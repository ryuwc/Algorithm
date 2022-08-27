import sys; sys.stdin = open('input_어디단어.txt', 'r')

for tc in range(int(input())):
    N, K = map(int, input().split())
    arr = []
    for _ in range(N):
        arr += [list(map(int, input().split()))]
    result = 0

    # 행 검색
    # result에 넣어줄 경우는 더하다가 마지막인덱스가 1이며 그 길이가 K인 경우,
    # 그리고, 더하다가 0을 만났는데, 더했던게 K인 경우이다.
    for i in range(N):
        sums = 0
        for j in range(N):
            if j == N-1 and arr[i][j] == 1:
                sums += 1
                if sums == K:
                    result += 1
            elif arr[i][j] == 1:
                sums += 1
            elif arr[i][j] == 0 and sums == K:
                sums = 0
                result += 1
            else:
                sums = 0

    # 열 검색
    for j in range(N):
        sums = 0
        for i in range(N):
            if i == N-1 and arr[i][j] == 1:
                sums += 1
                if sums == K:
                    result += 1
            elif arr[i][j] == 1:
                sums += 1
            elif arr[i][j] == 0 and sums == K:
                sums = 0
                result += 1
            else:
                sums = 0
    print(f'#{tc+1}', result)
