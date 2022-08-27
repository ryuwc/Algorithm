import sys; sys.stdin = open('1225.txt', 'r')

QSIZE = 9
Q = [0] * QSIZE
front = rear = 0           # 원형 큐는 0으로

def enqueue(item):
    # full-check -> rear == 마지막 인덱스
    global rear
    rear = (rear + 1) % QSIZE
    Q[rear] = item
def dequeue():
    global front
    # empty-check -> front == rear
    front = (front + 1) % QSIZE
    return Q[front]
def isEmpty():
    return front == rear
def isFull():
    return front == (rear + 1) % QSIZE

for tc in range(int(input())):
    front = rear = 0                 # 원형 큐는 0으로
    arr=list(map(int, input().split()))

    for val in arr:
        enqueue(val)

    count = 1
    while Q[rear]:
        val = dequeue()
        val -= count
        count = 1 if count == 5 else count + 1
        val = 0 if val < 0 else val
        enqueue(val)
    print(f'#{tc+1}', end=' ')
    while front != rear:
        print(dequeue(), end=' ')
    print()
