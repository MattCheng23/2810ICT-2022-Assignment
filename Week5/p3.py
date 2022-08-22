year1 = int(input("Year 1?"))
year2 = int(input("Year 2?"))
x = 0
for i in range(year1, year2):
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
        x += 1
n = (x * 366) + (year2 - year1 +1 - x)*365
print("Number of days:", n)

