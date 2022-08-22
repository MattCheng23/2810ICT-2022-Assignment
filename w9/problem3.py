s=input("Enter trip map referances: ")
list=s.strip().split()
import math
for i in range(len(list)):
    if len(list[i])>=2 and "A"<=list[i][0]<="Z":
        try:
            num=int(list[i][1:])
            if 1<=num<=26:
                pass
            else:
                print("Bad reference: %s" % list[i])
                exit()
        except:
            print("Bad reference: %s"%list[i])
            exit()
    else:
        print("Bad reference: %s" % list[i])
        exit()

total=0
for i in range(1,len(list)):
    disX=ord(list[i][0])-ord(list[i-1][0])
    disY=int(list[i][1:])-int(list[i-1][1:])
    dis=math.sqrt(disX*disX+disY*disY)
    total += dis

total=total*0.5
print("Total distance = %.1f km"%total)