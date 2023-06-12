import sys
from collections import deque


def main():
    sinput = sys.stdin.readline
    N = int(sinput())
    M = int(sinput())
    candidates = list(map(int, sinput().split()))

    # [학생번호, 추천횟수, 인덱스]
    rst = deque(maxlen=N)

    for i, val in enumerate(candidates):
        for info in rst:
            if info[0] == val:
                info[1] += 1
                break
        else:
            if len(rst) == N:
                rst = deque(sorted(list(rst), key=lambda x: (x[1], x[2])), maxlen=N)
            rst.append([val, 1, i])

    rst = [val[0] for val in rst]

    print(*sorted(rst))


if __name__ == '__main__':
    main()
