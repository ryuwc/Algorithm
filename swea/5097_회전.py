import sys; sys.stdin = open('input_회전.txt', 'r')

for tc in range(int(input())):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    Q = [0] * (N+1)
    front = rear = 0
    for i in nums:
        rear = (rear + 1) % (N+1)
        Q[rear] = i
    cnt = M
    while cnt:
        rear = (rear + 1) % (N+1)
        front = (front + 1) % (N+1)
        Q[rear] = Q[front]
        cnt -= 1

    print(f'#{tc+1}', Q[(front + 1) % (N+1)])
