positive_number = 0
a = 1

while a == 1:
    n = int(input("Enter a number:"))
    if n > 0:
        positive_number += 1
    elif n < 0:
        positive_number += 0
    else:
        break

print(positive_number, "Positive numbers were entered.")
