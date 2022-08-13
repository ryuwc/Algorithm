a, b = map(int, input().split())

result = a-((a/100)*b)

if result >= 100:
    print(0)
else:print(1)