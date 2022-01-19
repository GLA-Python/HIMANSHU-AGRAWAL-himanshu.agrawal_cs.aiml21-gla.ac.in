def expanding(lst1):
    temp = []
    for i in range(len(lst1) - 1):
        b = abs(lst1[i+1] - lst1[i])
        temp.append(b)
    for k in temp:
        if temp.count(k) >= 2:
            return False
    temp1 = temp.copy()
    temp.sort()
    if temp1 == temp:
        return True
    else:
        return False
# main driver code
lst = list(map(int, input().split()))
out = expanding(lst)
print(out)
