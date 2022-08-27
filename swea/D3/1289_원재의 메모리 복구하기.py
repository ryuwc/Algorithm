import sys; sys.stdin = open('input_원재.txt', 'r')

for tc in range(int(input())):
    memory = list(map(int, input()))
    N = len(memory)
    now = [0] * N

    cnt = 0

    for i in range(N):
        if memory[i] != now[i]:
            cnt += 1
            for j in range(i, N):
                now[j] = memory[i]
    print(f'#{tc+1}', cnt)
