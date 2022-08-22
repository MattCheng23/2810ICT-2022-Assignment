s = str(input("Input a string?"))

for i in range(10):
    s = s.replace(str(i), "_")

print("Output:", s)
