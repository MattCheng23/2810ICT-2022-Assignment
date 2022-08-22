n = input("Welcome to the Adder REPL.")
print(n)
import os

def getNum(dict,para):
    try:
        para=int(para)
    except:
        try:
            para=dict[para]
        except:
            para="error"
    return para

def isLetter(s):
    for p in s:
        if "a"<=p<="z" or "A"<=p<="Z":
            pass
        else:
            return 0
    return 1

def isNum(dict,para):
    try:
        para=int(para)
        return 1
    except:
        try:
            para=dict[para]
            return 1
        except:
            return 0

def isDictPara(dict,para):
    try:
        para=dict[para]
        return 1
    except:
        return 0


def handleSql(sql,dict):
    sql=sql.strip().split(" ")

    if sql[0]=="quit":
        print("Goodbye.")
        os._exit(0)

    elif sql[0]=="input":
        s=int(input("Enter a value for "+sql[1]+": "))
        dict[sql[1]]=s

    elif sql[0]=="print":
        num=getNum(dict,sql[1])
        if num=="error":
            print("%s is undefined."%sql[1])
        elif str(num)==sql[1]:
            print(sql[1])
        else:
            print("%s equals %d"%(sql[1],num))

    elif sql[1]=="gets":
        if isLetter(sql[0]) and isNum(dict,sql[2]):
            dict[sql[0]]=getNum(dict,sql[2])
        else:
            print("Syntax error.")

    elif sql[1]=="adds":
        if isDictPara(dict,sql[0]) and isNum(dict,sql[2]):
            dict[sql[0]]=dict[sql[0]]+getNum(dict,sql[2])
        else:
            print("Syntax error.")

    else:
        print("Syntax error.")

if __name__ == '__main__':
    dataDict={}
    while(1):
        sql=input("")
        try:
            handleSql(sql,dataDict)
        except:
            print("Syntax error.")
