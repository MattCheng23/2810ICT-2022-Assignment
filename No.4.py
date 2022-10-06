import time
import csv
import matplotlib.pyplot as plt

fileName = 'DataBase.csv'

x = []
y = []

with open(fileName, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:

        xtime = time.mktime(time.strptime(row[0], "%y%m%d_%H:%M:%S"))

        if row[2].isdigit():
            x.append(xtime)
            y.append(row[2])
        else:
            print("Wrong type: " + str(row))

deta = int(x[0])
for j in range(len(x)):
    x[j] = int(x[j]) - deta
    y[j] = int(y[j])

plt.xlabel("Time(s)")
plt.ylabel("Ug(TSI_PM2.5)")

plt.plot(x, y, label='TSI_PM2.5', linewidth=2)

plt.legend()
plt.show()
