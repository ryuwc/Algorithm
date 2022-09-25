

c, r, w, h = map(int, input().split())

result = min(abs(c-w), abs(r-h), c-0, r-0)
print(result)