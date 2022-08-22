n = int(input("Enter a positive number"))

n1 = 0
n2 = 1
count = 0

if n == 1:
    print(n1)
else:
    for i in range(0, n):
        nth = n1 + n2
        print(n1, end=" , ")
        n1 = n2
        n2 = nth
        count += 1
        if count == 4:
            print()
            count = 0


