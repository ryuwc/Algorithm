import sys;

while True:
    N, *info = map(int, sys.stdin.readline().strip().split())
    if N == 0:
        break

    info.append(0)
    S = []
    rst = 0
    for i in range(N+1):
        # 스택에 높이와 인덱스를 저장할건데 pointer는 인덱스를 가리킴
        # 이때 저장하는 인덱스는 단순히 그 높이의 인덱스가 아니라 현재 높이로 만들수 있는 전의 인덱스를 가르킴
        pointer = i
        # 현재 높이가 스택에 마지막 요소의 높이보다 작으면 rst값을 갱신
        while S and info[i] < S[-1][0]:
            h, d = S.pop()
            # 이때 포인터를 d로 가르키게함 자세한 설명은 후기에..
            pointer = d
            tmp = h * (i-d)
            rst = max(rst, tmp)
        S.append((info[i], pointer))

    print(rst)