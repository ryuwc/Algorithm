import sys


def solve(ground_copy, hei, dart_copy):
    tmp_time = 0

    for i in range(N):
        for j in range(M):
            now_dart = ground_copy[i][j]
            if now_dart > hei:
                gap = now_dart - hei
                tmp_time += 2 * gap
                dart_copy += gap
            elif now_dart < hei:
                gap = hei - now_dart
                tmp_time += gap
                dart_copy -= gap

            if tmp_time > time:
                return -1, -1

    if dart_copy < 0:
        return -1, -1
    else:
        return tmp_time, hei


N, M, dart = map(int, sys.stdin.readline().strip().split())
ground = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
time = 9e9
height = 0

all_dart = sum(map(sum, ground)) + dart
max_height = max(map(max, ground))
min_height = min(map(min, ground))

for hei in range(min_height, min(257, (all_dart // (N * M)) + 1)):
    dart_copy = dart
    a, b = solve(ground, hei, dart_copy)
    if a == -1:
        continue
    else:
        if time >= a:
            time = a
            height = max(height, b)

print(time, height)
