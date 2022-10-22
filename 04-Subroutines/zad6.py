#6.	Define a function that displays numbers in the layout as below (like on a phone keypad). Apply an loop statement. Then call the function.
#1 2 3
#4 5 6
#7 8 9

def layout():
    for i in range (1,4):
        print(i,end= " ")
    print()
    for i in range (4,7):
        print(i,end=" ")
    print()
    for i in range (7,10):
        print(i,end=" ")
    print()

def layout2():
    for x in range(1,10,1):
        if x%3==1:
            print(x,end= " ")
        elif x%3==2:
            print(x,end=" ")
        else x%3==3:
            print(x,end=" ")

def layout3():
    for i in range(1,10):
        print(i, end= " ")
        if i==3 or i==6:
            print()

def layout4():
    for i in range(1,10):
        print(i, end=" ")
        if i%3==0:
            print()

layout()