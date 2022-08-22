f = open(input("File name:"), "r")
lines = f.readlines()
for line in lines:
    ls = list(map(int, line.split()))
    if ls[1]- ls[0] == ls[-1] - ls[-2] and ls[1]- ls[0] == ls[2] - ls[1]:
        print(ls," True")
    else:
        print(ls,"False")


f.close()
