import sys; sys.stdin = open('5186.txt')

for tc in range(int(input())):
    N = float(input())
    bin_lst = []
    while 1:
        val = N * 2
        mod = val % 1
        N = mod
        tmp = int(val)
        bin_lst.append(tmp)
        if val == 1.0:
            break
    bin_lst = list(map(str, bin_lst))
    if len(bin_lst) >= 13:
        print(f'#{tc+1}', 'overflow')
    else:
        print(f'#{tc+1}', ''.join(bin_lst))
