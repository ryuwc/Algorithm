import sys

N = int(sys.stdin.readline())

bp = 0
for i in range(666, sys.maxsize):
    if '666' in str(i):
        bp += 1
    if bp == N:
        print(i)
        break
