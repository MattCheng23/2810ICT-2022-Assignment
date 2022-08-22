a = 0
while a ==0:
    string = str(input("Enter a string: "))
    lower = string.lower()
    split = lower.split()
    split.sort(reverse=True)

    output = ("output:" + " ".join(split))
    print(output)
