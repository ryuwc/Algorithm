import sys
from collections import defaultdict

sinput = sys.stdin.readline

N, M = map(int, sinput().strip().split())
person_dict = defaultdict(int)
for _ in range(N):
    person = sinput().rstrip()
    person_dict[person] += 1

for _ in range(M):
    person = sinput().rstrip()
    person_dict[person] += 1

rst = []

for key, value in person_dict.items():
    if value > 1:
        rst.append(key)

print(len(rst))
for name in sorted(rst):
    print(name)
