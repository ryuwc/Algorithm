
N, K = map(int, input().split())

arr = [i for i in range(1, N+1)]

new_arr = []

now = 0
while arr:
    now = (now+K-1)%len(arr)
    new_arr.append(arr.pop(now))

rst = '<'+', '.join(map(str, new_arr)) + '>'

print(rst)