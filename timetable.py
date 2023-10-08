num = input("Create a time table for number _")

def createTimeTable(num):
    for i in range(1, num+1):
        print("|", end='\t')
        for x in range(1, num+1):
            print(x * i, end='\t')
        print("|")

createTimeTable(int(num))