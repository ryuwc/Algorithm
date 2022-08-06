
# 1번 방식 time-out... 
def func(lst):
    lst = sorted(list(lst))
    result = []
    l = -1
    r = 0
    while l < len(lst) - 2:
        l += 1
        for k in range(l+1, len(lst)-1):
            r += 1
            for i in range(k+1, len(lst)):
                if lst[l] + lst[k] + lst[i] == 0 and sorted(list((lst[l], lst[k], lst[i]))) not in result:
                    result.append(sorted(list((lst[l], lst[k], lst[i]))))
                else:
                    continue
    
    return result
    
    
    


print(func([1,2,-2,-1]))
print(func([-1,0,1,2,-1,-4]))
print(func([-1,0,1,0]))
print(func([-2,0,1,1,2]))