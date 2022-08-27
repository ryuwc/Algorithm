import sys; sys.stdin = open('input_큐_숫자카드.txt', 'r')

# 정석대로 풀이
for tc in range(1, int(input())+1):
    N = int(input())
    q = [0]*1000000        # 초기 q를 얼마나 잡아줘야 되는지... 10만이면 부족함, 그래서 100만으로 잡음
    front = rear = -1
    for i in range(1, N+1):
        rear += 1
        q[rear] = i

    while True:
        front += 1
        if rear == front:   # front와 rear가 같아지는지 확인해야하는 지점
            break
        front += 1
        val = q[front]
        rear += 1
        q[rear] = val
        if rear == front:   # front와 rear가 같아지는지 확인해야하는 지점
            break

    print(f'#{tc}', q[rear])

