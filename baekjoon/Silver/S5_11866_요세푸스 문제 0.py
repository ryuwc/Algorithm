import sys

N, K = map(int, sys.stdin.readline().strip().split())
people = [i for i in range(1, N + 1)]

rst = []
idx = 0
while people:
    idx = (idx + K - 1) % len(people)
    rst.append(people.pop(idx))

print('<' + ', '.join(map(str, rst)) + '>')
