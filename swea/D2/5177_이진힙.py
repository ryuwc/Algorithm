import sys; sys.stdin = open('input_이진힙.txt', 'r')



def push(item):
    global last
    last += 1
    h[last] = item

    c, p = last, last // 2
    while True:
        if p > 0 and h[c] < h[p]:
            h[c], h[p] = h[p], h[c]
            c = p
            p = c // 2
        else:
            break

def pop():
    ret = h[1]
    global last
    h[1] = h[last]
    last -= 1

    p, c = 1, 2

    while c <= last:
        if c + 1 <= last and h[c] > h[c+1]:
            c += 1

        if h[c] <= h[p]: break

        h[c], h[p] = h[p], h[c]
        p = c
        c = p*2

    return ret

for tc in range(int(input())):
    size = 1000
    h = [0] * size
    last = 0

    V = int(input())
    data = list(map(int, input().split()))

    for val in data:
        push(val)

    p_lst = []
    c = V
    while True:
        p = c // 2
        p_lst.append(h[p])
        c = p
        if p == 0:
            break
    print(f'#{tc+1}', sum(p_lst))


