f = open(input("File name:"), "r")
count = 0
lines = f.readlines()
for line in lines:
    count += 1
    ls = list(map(int,line.split()))
    print("The average of line", count,"is",sum(ls)/len(ls))
f.close()
