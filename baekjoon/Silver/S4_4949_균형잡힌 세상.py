import sys

def solve():
    if st == '.':
        return
    for s in stt:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if not stack:
                return print('no')
            elif stack[-1] == '(':
                stack.pop()
            else:
                return print('no')
        elif s == ']':
            if not stack:
                return print('no')
            elif stack[-1] == '[':
                stack.pop()
            else:
                return print('no')
    if stack:
        return print('no')
    else:
        return print('yes')


if __name__ == '__main__':
    while True:
        rhkfgh = ['(', '[', ')', ']']
        st = sys.stdin.readline().rstrip()

        if st == '.':
            exit()

        stt = []
        for s in st:
            if s in rhkfgh:
                stt.append(s)

        stack = []

        solve()

