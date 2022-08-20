import sys; sys.stdin = open('input_쇠막대기.txt', 'r')

for tc in range(int(input())):
    stick = list(input())

    pipe = 0
    count = 0

    stack = [0] * 100000
    top = -1

    for i in stick:
        if i == '(' and stack[top] == '(':
            top += 1
            stack[top] = i
            pipe += 1
            count += 1
        elif i == '(':
            top += 1
            stack[top] = i
        elif i == ')' and stack[top] == '(':
            top += 1
            stack[top] = i
            count += pipe
        elif i == ')' and stack[top] == ')':
            pipe -= 1
            top += 1
            stack[top] = i
    print(f'#{tc+1}', count)


