N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]

max_r = max_c = 0
for n in info:                  # 1000행, 1000열을 미리 만들기 싫어서 최대 행값과 열값을 뽑아준다.
    if (n[2]+n[0]) > max_c:
        max_c = (n[2]+n[0])
    if (n[3]+n[1]) > max_r:
        max_r = (n[3]+n[1])

arr = [[0]*(max_c+1) for _ in range(max_r+1)]

for s in range(N):
    r, c, w, h = info[s][0], info[s][1], info[s][2], info[s][3],
    for i in range(c, c+h):              # 이 부분에서 시간초과 문제가 발생한다.
        arr[i][r:r+w] = [s+1]*w          # 열을 하나하나 바꾸지말고, 원하는 만큼의 열을 한번에 바꿔준다.
# for line in arr:
#     print(*line)
for num in range(1, N+1):
    sums = 0
    for i in arr:
        sums += i.count(num)

    print(sums)