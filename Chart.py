import csv
import matplotlib.pyplot as plt

File = open('DataBase.csv')
Reader = csv.reader(File)
Data = list(Reader)
length_1 = len(Data)
length_2 = len(Data[0])

x = list()
y = list()

for i in range(1, length_1):  
    x.append(Data[i][0])  
    y.append(Data[i][1]) 

plt.plot(x, y) 
plt.show()