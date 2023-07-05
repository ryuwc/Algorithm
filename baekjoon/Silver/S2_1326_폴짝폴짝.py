import sys
from collections import deque


def bfs(a, b, arr):
    N = len(arr)
    Q = deque()
    Q.append((a - 1, 0))
    visit = [False] * N
    visit[a - 1] = True

    while Q:
        now, cnt = Q.popleft()
        if now == b - 1:
            return cnt
        step = arr[now]
        for i in range(-(now // step), (N - 1) // step + 1):  # i는 배수
            val = now + step * i
            if 0 <= val < N and not visit[val]:
                Q.append((val, cnt + 1))
                visit[val] = True

    return -1


def main():
    N = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    a, b = map(int, sys.stdin.readline().strip().split())

    print(bfs(a, b, arr))


if __name__ == '__main__':
    main()
