l1 = input("List 1: ").split()
l2 = input("List 2: ").split()
def newlist(ls1,ls2):
    output = []
    for i in ls1:
        if i in ls1 and i in ls2:
            if i not in output:
                output.append(i)
    return output

list1 = list(map(int, l1))
list2 = list(map(int, l2))
print(newlist(list1, list2))
