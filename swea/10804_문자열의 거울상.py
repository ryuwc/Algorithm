
T = int(input())
for tc in range(1, T+1):
    strs = list(input())

    for i in range(len(strs)):
        if strs[i] == 'b':
            strs[i] = 'd'
        elif strs[i] == 'd':
            strs[i] = 'b'
        elif strs[i] == 'p':
            strs[i] = 'q'
        elif strs[i] == 'q':
            strs[i] = 'p'
    print(f'#{tc}', ''.join(strs[::-1]))
