f1 = open(input("Source file name:"))
f2 = open(input("Target file name:"), mode='w')


for line in f1:
    if line != '\n' and line[0] not in "123456789":
        f2.write(line)


f1.close()
f2.close()

