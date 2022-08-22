f1 = open(input("Source file name:"))
f2 = open(input("Target file name:"), mode='w')
count = 0

for line in f1:
    if line != '\n':
        f2.write(line)
    else:
        count += 1
print("Lines removed:", count)
f1.close()
f2.close()

