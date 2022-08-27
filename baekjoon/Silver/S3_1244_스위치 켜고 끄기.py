
N = int(input())
arr = list(map(int, input().split()))
P = int(input())

for i in range(P):
    s, n = map(int, input().split())
    if s == 1:
        for j in range(n-1, N, n):
            if arr[j] == 1:
                arr[j] = 0
            else:
                arr[j] = 1

    elif s == 2:
        l, r = n-2, n
        while True:
            if l < 0 or r >= N:
                break
            if arr[l] != arr[r]:
                break
            else:
                l -= 1
                r += 1
        for j in range(l+1, r):
            if arr[j] == 1:
                arr[j] = 0
            else:
                arr[j] = 1

for i in range(0, N, 20):
    print(*arr[i:i+20])

