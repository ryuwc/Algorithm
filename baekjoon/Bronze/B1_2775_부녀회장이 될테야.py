T = int(input())
for tc in range(T):
    k = int(input())
    n = int(input())
    people = [i for i in range(1, n + 1)]
    for _ in range(k):
        for i in range(1, n):
            people[i] += people[i - 1]
    print(people[-1])
