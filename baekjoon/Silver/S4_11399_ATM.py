import sys

sinput = sys.stdin.readline

N = int(sinput().rstrip())
times = list(map(int, sinput().rstrip().split()))

times.sort()

rst = 0
for i in range(N):
    rst += sum(times[:i+1])

print(rst)