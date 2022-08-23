import sys; sys.stdin = open('4874.txt', 'r')

def cal(codes):
    stack = []
    for i in codes:
        if i.isdigit():
            stack.append(i)
        elif i == '+':           # 연산자가 나오면 (스택의 두번째 pop) 연산자 (스택의 첫번째 pop) 값을 넣어준다.
            if len(stack) == 1:  # 연산자가 나오면 스택에는 최소 2개의 숫자가 있어야 하는데, 없는 경우 error를 리턴
                return 'error'
            else:
                a = stack.pop()
                b = stack.pop()
                c = int(b) + int(a)
                stack.append(c)
        elif i == '-':
            if len(stack) == 1:
                return 'error'
            else:
                a = stack.pop()
                b = stack.pop()
                c = int(b) - int(a)
                stack.append(c)
        elif i == '*':
            if len(stack) == 1:
                return 'error'
            else:
                a = stack.pop()
                b = stack.pop()
                c = int(b) * int(a)
                stack.append(c)
        elif i == '/':
            if len(stack) == 1:
                return 'error'
            else:
                a = stack.pop()
                b = stack.pop()
                c = int(b) // int(a)
                stack.append(c)
    if len(stack) > 1:      # 스택에 하나 이상의 요소가 담겨있다면 error리턴
        return 'error'
    else:
        return int(stack[-1])

for tc in range(int(input())):
    codes = list(map(str, input().rstrip('.').split()))

    print(f'#{tc+1}', cal(codes))


#1 84
#2 error
#3 168




