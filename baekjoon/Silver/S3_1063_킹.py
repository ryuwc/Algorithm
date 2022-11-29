import sys; from collections import deque

graph = {
    'R': [0, 1],
    'L': [0, -1],
    'B': [1, 0],
    'T': [-1, 0],
    'RT': [-1, 1],
    'LT': [-1, -1],
    'RB': [1, 1],
    'LB': [1, -1]
}

king, stone, N = sys.stdin.readline().strip().split()
N = int(N)
king = [8-int(king[1]), ord(king[0])-65]
stone = [8-int(stone[1]), ord(stone[0])-65]

Q = deque()
Q.append(king)
move = []
for _ in range(N):
    m = sys.stdin.readline().strip()
    move.append(m)

for v in move:
    tmp1 = king[1] + graph[v][1]
    tmp2 = king[0] + graph[v][0]
    if 0 <= tmp1 < 8 and 0 <= tmp2 < 8:
        if tmp1 == stone[1] and tmp2 == stone[0]:
            tmp_stone1 = stone[1] + graph[v][1]
            tmp_stone2 = stone[0] + graph[v][0]
            if 0 <= tmp_stone1 < 8 and 0 <= tmp_stone2 < 8:
                stone[1] = tmp_stone1
                stone[0] = tmp_stone2
                king[1] = tmp1
                king[0] = tmp2
        else:
            king[1] = tmp1
            king[0] = tmp2

print(f'{chr(king[1]+65)}{8-king[0]}')
print(f'{chr(stone[1]+65)}{8-stone[0]}')



# print(move)
# print(king, stone)