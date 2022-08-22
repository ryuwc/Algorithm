import sys; sys.stdin = open('input_방 배정.txt', 'r')


N, K = map(int, input().split())
student = [[0]*2 for _ in range(6)]
for _ in range(N):
    s, y = map(int, input().split())
    student[y-1][s-1] += 1
# print(student)      # [[2, 1], [1, 2], [3, 1], [1, 0], [2, 1], [1, 1]]
rooms = 0
for i in range(6):
    for j in range(2):
        # if student[i][j] == 0:
        #     continue
        if student[i][j] % K == 0:
            rooms += student[i][j]/K
        else:
            rooms += student[i][j]//K +1

print(int(rooms))


