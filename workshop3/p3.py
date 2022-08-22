int1 = int(input("Enter integer 1:"))
int2 = int(input("Enter integer 2:"))
int3 = int(input("Enter integer 3:"))

if int1 < int2 and int1 < int3:
    if int2 < int3:
        print(int3, int2, int1)
    else:
        print(int2, int3, int1)
elif int2 < int1 and int2 < int3:
    if int1 < int3:
        print(int3, int1, int2)
    else:
        print(int1, int3, int2)
elif int3 < int1 and int3 < int2:
    if int1 < int2:
        print(int2, int1, int3)
    else:
        print(int1, int2, int3)
