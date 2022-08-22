n = str(input("Input a list: ")).split()
def rotatelst(list):
    for i in range(len(list)):
        list = list[1:]+list[:1]
        print(list)
lst = list(map(int,n))
print(lst)
rotatelst(lst)
