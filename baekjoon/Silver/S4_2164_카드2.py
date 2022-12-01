from collections import deque

# 사실 큐 문제는 deque사용하면 편하다;

N = int(input())
Q = deque([i for i in range(1, N+1)])

# 큐에 하나만 남을 때 까지 두가지 작업 반복
while len(Q) > 1:
    Q.popleft()
    Q.append(Q.popleft())

print(*Q)