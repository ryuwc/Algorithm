import sys; sys.stdin = open('5099.txt', 'r')

for tc in range(int(input())):
    N, M = map(int, input().split())
    tmp_pizza = list(map(int, input().split()))
    pizza = []
    for i in range(M):          # 피자의 번호를 알아야 하기 때문에 인덱스 번호를 같이 저장(2차원 리스트)
        pizza.append([i, tmp_pizza[i]])

    Q = []
    for _ in range(N):          # 화로의 크기만큼 피자를 넣어줌
        Q.append(pizza[_])
    for _ in range(N):          # 넣어진 피자를 피자리스트에서 빼줌
        pizza.pop(0)

    while len(Q) > 1:                   # 피자가 1개 남을 때 종료
        cheese = Q.pop(0)               # 피자를 빼서 확인하는 작업
        if cheese[1]//2 != 0:           # 피자의 치즈가 //2를 해서 0이 안되었다면
            cheese[1] = cheese[1]//2    # 치즈에 //2를 해서 다시 넣어줌
            Q.append(cheese)
        elif cheese[1]//2 <= 0:         # 치즈가 0이되고
            if pizza:                   # 남아있는 피자가 있는 경우
                remain = pizza.pop(0)   # 남아있는 피자의 첫 번째 인덱스에 있는 걸 넣어줌
                Q.append(remain)
    print(f'#{tc+1}', Q[0][0]+1)

