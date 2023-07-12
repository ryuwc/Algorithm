import sys

a, b = map(int, sys.stdin.readline().strip().split())

min_ab = min(a, b)
max_ab = a if a > b else b
rst1 = 0
rst2 = 0

for i in range(min_ab, 0, -1):
    if a % i == 0 and b % i == 0:
        rst1 = i
        break

for i in range(min_ab, a * b + 1, min_ab):
    if i % a == 0 and i % b == 0:
        rst2 = i
        break

print(rst1)
print(rst2)
