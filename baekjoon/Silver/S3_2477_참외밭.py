
N = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]

max_w = 0
max_h = 0
max_w_idx = 0
max_h_idx = 0

for i in range(6):
    if arr[i][0] == 1 or arr[i][0] == 2:
        if max_w < arr[i][1]:
            max_w = arr[i][1]
            max_w_idx = i
    elif arr[i][0] == 3 or arr[i][0] == 4:
        if max_h < arr[i][1]:
            max_h = arr[i][1]
            max_h_idx = i

min_r = abs(arr[(max_w_idx - 1) % 6][1] - arr[(max_w_idx + 1)%6][1])
min_c = abs(arr[(max_h_idx - 1) % 6][1] - arr[(max_h_idx + 1)%6][1])

area = (max_w * max_h) - (min_r * min_c)

result = area * N

print(result)

