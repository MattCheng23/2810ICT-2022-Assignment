n = int(input("Enter a positive number:"))

for i in range(1, n + 1):
    for j in range(1, n+1):
        if i+j < n:
            print(" ", end=" ")
        else:
            print("*",end= " ")
    print()
