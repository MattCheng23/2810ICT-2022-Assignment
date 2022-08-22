file_add = input("File name:")
f = open(file_add, encoding='utf-8')

w = 0


for line in f:
    if line in "a-z":
        print(line)

    word = line.split()
    w = w + len(word)

else:
    print("Words:%s" % w)


f.close()