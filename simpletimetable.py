num = input("Create a simple time table for number _")

def createsimpletimetable(num):
    for x in range(1,13):
        print(num, " x ", x, " = ", int(num) * x)

createsimpletimetable(num)