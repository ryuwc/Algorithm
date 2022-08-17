
N, k = map(int, input().split())
point = list(map(int, input().split()))

c = [0]*10001
arr = [0]*N
for i in point:
    c[i] += 1
for i in range(1, len(c)):
    c[i] += c[i-1]
for i in range(N-1, -1, -1):
    c[point[i]] -= 1
    arr[c[point[i]]] = point[i]
print(arr[N-k])