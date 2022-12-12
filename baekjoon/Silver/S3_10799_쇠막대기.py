import sys

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
print(count)
