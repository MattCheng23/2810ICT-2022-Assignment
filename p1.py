marks = float(input("Please Enter your marks"))

if marks >= 85:
    grade = "7"
elif 85 > marks >= 75:
    grade = "6"
elif 75 > marks >= 65:
    grade = "5"
elif 65 > marks >= 50:
    grade = "4"
elif marks < 50:
    grade = "F"
print("grade awarded", grade)
