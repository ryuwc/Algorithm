a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

lst1 = [a, b, c, d]
lst2 = [e, f]
lst1.sort()
lst2.sort()
print(sum(lst1[1:])+lst2[1])