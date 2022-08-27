
w, h = map(int, input().split())
p, q = map(int, input().split())
time = int(input())

x = p + time
y = q + time
                # 개미는 일정한 칸 안에서 움직인다.
move_x = []     # [0, 1, 2, 3, 4, 5, 4, 3, 2, 1]
move_y = []     # [0, 1, 2, 3, 2, 1]

for i in range(w):
    move_x.append(i)
for i in range(w, 0, -1):
    move_x.append(i)

for i in range(h):
    move_y.append(i)
for i in range(h, 0, -1):
    move_y.append(i)

x_ = move_x[x%(2*w)]   # 즉, 개미위치 + time의 인덱스를 위의 리스트 안에서 돌려주면 된다.
y_ = move_y[y%(2*h)]

print(x_, y_)