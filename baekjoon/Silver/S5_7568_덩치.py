import sys

T = int(sys.stdin.readline())
lst = []
for tc in range(T):
    lst.append(list(map(int, sys.stdin.readline().split())))
for i in range(T):
    rank = 1
    for j in range(T):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            rank += 1
    print(rank, end=' ')

