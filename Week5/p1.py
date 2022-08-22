a = 1
ls = " "
n = " "
while a == 1:
    n = str(input("Enter a String:"))
    if len(n) > len(ls):
        ls = n
    elif n[0] == "A":
        break
print("Longest was:", ls)
