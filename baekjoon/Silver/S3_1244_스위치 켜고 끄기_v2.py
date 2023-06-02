def main():
    N = int(input())
    arr = list(map(int, input().split()))
    P = int(input())

    for _ in range(P):
        s, n = map(int, input().split())
        if s == 1:
            for j in range(n - 1, N, n):
                arr[j] = 1 - arr[j]  # arr[j]가 0이면 1을, 1이면 0을 할당
        elif s == 2:
            l, r = n - 2, n  # 동시에 변수 초기화
            while 0 <= l and r < N and arr[l] == arr[r]:
                l -= 1
                r += 1
            for j in range(l + 1, r):
                arr[j] = 1 - arr[j]

    for i in range(0, N, 20):
        print(*arr[i:i + 20])


if __name__ == '__main__':
    main()
