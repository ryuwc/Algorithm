import sys; sys.stdin = open('input_의석이의세로.txt', 'r')

for tc in range(int(input())):
    a = list(input())
    b = list(input())
    c = list(input())
    d = list(input())
    e = list(input())

    ans = ['']*1000

    for i in range(len(a)):
        ans[i * 5] = a[i]
    for i in range(len(b)):
        ans[(i * 5) + 1] = b[i]
    for i in range(len(c)):
        ans[(i * 5) + 2] = c[i]
    for i in range(len(d)):
        ans[(i * 5) + 3] = d[i]
    for i in range(len(e)):
        ans[(i * 5) + 4] = e[i]
    print(f'#{tc+1}', ''.join(map(str, ans)))
