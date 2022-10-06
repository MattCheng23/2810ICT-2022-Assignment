import time
import csv
import matplotlib.pyplot as plt

fileName = 'DataBase.csv'

xtime = []
yvalue = []

with open(fileName, 'r') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:

        xtimestamp = time.mktime(time.strptime(row[0], "%y%m%d_%H:%M:%S"))

        if row[2].isdigit():
            xtime.append(xtimestamp)
            yvalue.append(row[2])
        else:
            print("Wrong type: " + str(row))

deta = int(xtime[0])
for j in range(len(xtime)):
    xtime[j] = int(xtime[j]) - deta
    yvalue[j] = int(yvalue[j])

plt.xlabel("Time(s)")
plt.ylabel("Ug(TSI_PM2.5)")

plt.plot(xtime, yvalue, label='TSI_PM2.5', linewidth=2)

plt.legend()
plt.show()
