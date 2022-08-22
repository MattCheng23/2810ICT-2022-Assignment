file_add = input("File name:")
f = open(file_add, encoding='utf-8')
c = 0
w = 0
l = 0

for line in f:
    c = c + len(line)
    word = line.split()
    w = w + len(word)
    l = l + 1
else:
    print("Characters:%s" % c)
    print("Words:%s" % w)
    print("Lines:%s" % l)

f.close()
