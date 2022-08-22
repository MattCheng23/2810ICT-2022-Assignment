l1 = input("List 1: ").split()
l2 = input("List 2: ").split()
l3 = list(map(int,l1+l2))
a = 0

while a == 0:
    l3.sort()
    l3.reverse()
    print(l3)
    break



