import sys
from collections import defaultdict

T = int(sys.stdin.readline().strip())
for tc in range(T):
    N = int(sys.stdin.readline().strip())

    cloths = []
    for _ in range(N):
        a, b = map(str, sys.stdin.readline().strip().split())
        cloths.append([a, b])

    category_count = defaultdict(int)

    for cloth in cloths:
        category_count[cloth[1]] += 1

    rst = 1
    for count in category_count.values():
        rst *= (count + 1)

    print(rst - 1)
