lst = list(map(int, input().split()))

lst.sort()

t1 = lst[0]+lst[3]
t2 = lst[1]+lst[2]

lst1 = [t1, t2]

print(max(lst1)-min(lst1))

