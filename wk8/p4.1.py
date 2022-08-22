l1 = input("List 1: ").split()
l2 = input("List 2: ").split()

l1.sort(reverse=True)
l2.sort(reverse=True)

sort = []
p1 = p2 = 0
while p1 < len(l1) or p2 < len(l2):
    if p1 == len(l1):
        sort.append(l2[p2])
        p2 += 1
    elif p2 == len(l2):
        sort.append(l1[p1])
        p1 += 1
    elif l1[p1] > l2[p2]:
        sort.append(l1[p1])
        p1 += 1
    else:
        sort.append(l2[p2])
        p2 += 1
result = list(map(lambda x: int(x), sort))
print(result)



