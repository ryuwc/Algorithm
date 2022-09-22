import sys; sys.stdin = open('sample_input_화물도크.txt', 'r')

for tc in range(int(input())):
    N = int(input())
    info = []
    for _ in range(N):
        s, e = map(int, input().split())
        info += [[s, e]]
    info.sort(key=lambda x:x[1])
    result = 0
    for k in range(N):
        tmp = []
        for i in range(k, N):
            if not tmp:
                tmp.append(info[i])
                continue
            elif tmp[-1][1] <= info[i][0]:
                tmp.append(info[i])
        result = max(result, len(tmp))

    print('#{}'.format(tc+1), result)
    # print(info)
