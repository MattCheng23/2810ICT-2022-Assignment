hours = int(input("How many hours were worked?"))
cars = int(input("Total number of cars sold for the week?"))
if cars <= 5 and hours > 37:
    salary = (36.25 * 37) + (1.5 * 36.25 * (hours - 37))

elif cars > 5 and hours > 37:
    salary = (36.25 * 37) + (1.5 * 36.25 * (hours - 37) + (cars - 5) * 200)

elif cars > 5 and hours < 37:
    salary = (36.25 * hours) + (cars - 5) * 200

elif cars < 5 and hours < 37:
    salary = (36.25 * hours)

print("Salary", salary)
