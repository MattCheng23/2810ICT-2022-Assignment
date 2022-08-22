list1 = [int(n) for n in input("List1:").split()]
list2 = [int(n) for n in input("List2:").split()]
a = 0
sum1 = list1[0]+list1[-1]
sum2 = list2[0]+list2[-1]
if len(list1) == 1:
    sum1 = sum1/2
    if sum1 > sum2:
        print("Output:", int(sum1))
    elif sum1 < sum2:
        print("Output:", int(sum2))
else:
    if sum1 > sum2:
        print("Output:", sum1)

if len(list2) == 1:
    sum2 = sum2/2
    if sum1 > sum2:
        print("Output:", int(sum1))
    elif sum1 < sum2:
        print("Output:", int(sum2))
else:
    if sum1 < sum2:
        print("Output:", sum2)

if sum1 == sum2:
    print("Output:same")
