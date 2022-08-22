f = open(input("File name:"))
f1 = f.readlines()
print("Output:")
for i in range(2):
    print(f1[i],end="")
for x in range(-2,0,1):
    print(f1[x],end="")

f.close()
