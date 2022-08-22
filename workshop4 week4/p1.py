n = int(input("Enter a number:"))
positive_number = 0

while n > 0 or n < 0:
    n = int(input("Enter a number:"))
    if n > 0 and n == 0:
        positive_number += 1
    elif n == 0:
        print(positive_number, "Positive numbers were entered.")
