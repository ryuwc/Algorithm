import sys; sys.stdin = open('input_사칙연산.txt', 'r')

def solve(v):
    for a, b, c, d in calc[::-1]:
        if b == '+':
            tree[int(a)] = tree[int(c)] + tree[int(d)]
        elif b == '-':
            tree[int(a)] = tree[int(c)] - tree[int(d)]
        elif b == '*':
            tree[int(a)] = tree[int(c)] * tree[int(d)]
        elif b == '/':
            tree[int(a)] = tree[int(c)] // tree[int(d)]

for tc in range(1, 11):
    N = int(input())
    tree = [0] * 1001
    tree_cal = [''] * 1001

    calc = []

    for n in range(N):
        n = input().split()
        if len(n) == 2:
            tree[int(n[0])] = int(n[1])
        else:
            calc.append(n)

    solve(1)
    print(f'#{tc}', tree[1])
