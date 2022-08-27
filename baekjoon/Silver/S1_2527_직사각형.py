import sys


def check(x1, y1, p1, q1, x2, y2, p2, q2):
    if q2 < y1 or q1 < y2 or x1 > p2 or p1 < x2:
        return 'd'
    if x2 == p1:
        if q1 == y2 or y1 == q2:
            return 'c'
        else:
            return 'b'
    if x1 == p2:
        if y1 == q2 or q1 == y2:
            return 'c'
        else:
            return 'b'
    if q1 == y2:
        if x2 == p1 or x1 == p2:
            return 'c'
        else:
            return 'b'
    if q2 == y1:
        if p1 == x2 or p2 == x1:
            return 'c'
        else:
            return 'b'
    return 'a'

for _ in range(4):
    a, b, c, d, e, f, g, h = map(int, input().split())
    print(check(a, b, c, d, e, f, g, h))
