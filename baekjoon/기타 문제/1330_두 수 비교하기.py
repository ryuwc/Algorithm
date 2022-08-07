lst = list(map(int, input().split()))

a = lst[0]
b = lst[1]

if a > b:
    print('>')
elif a < b:
    print('<')
elif a == b:
    print('==')