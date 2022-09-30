import sys; sys.stdin = open('1251.txt')
import math

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

for tc in range(int(input())):
    N = int(input())
    info = [[0, 0] for _ in range(N+1)]
    r_info = list(map(int, input().split()))
    c_info = list(map(int, input().split()))
    for _ in range(N):
        dis_r = r_info[_]
        dis_c = c_info[_]
        info[_+1][0] = dis_r
        info[_+1][1] = dis_c
    E = float(input())
    p = [i for i in range(N+1)]
    edges = []
    for fir in range(1, N+1):
        for sec in range(fir+1, N+1):
            u = fir
            v = sec
            cost = 0
            if info[fir][0] == info[sec][0]:
                cost = abs(info[fir][1] - info[sec][1])
            elif info[fir][1] == info[sec][1]:
                cost = abs(info[fir][0] - info[sec][0])
            else:
                cost = math.sqrt((abs(info[fir][0] - info[sec][0]))**2 + (abs(info[fir][1] - info[sec][1]))**2)
            edges.append([u, v, cost])

    edges.sort(key=lambda x:x[2], reverse=True)

    # for line in edges:
    #     print(line, line[2]**2)

    mst = []
    rst = 0
    cnt = N-1
    while cnt:
        u, v, weight = edges.pop()
        a = find_set(u)
        b = find_set(v)
        if a == b: continue
        rst += (weight**2)*E
        mst.append([u, v, weight])

        p[a] = b
        cnt -= 1

    print(f'#{tc+1}', round(rst))
