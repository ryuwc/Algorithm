
N = int(input())
arr = [0]*N
for i in range(N):
    arr[i] = int(input())

for i in range(1, N):
    for j in range(0, N-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

for i in range(N):
    print(arr[i])
