
words = input()

visit = [0]*26

for word in words:
    visit[ord(word)-97] += 1

print(*visit)
