#9.	A user enters two integer numbers from the keyboard. Write a program that checks if at least one of them is positive.

x = (int(input("x: ")))
y = (int(input("y: ")))

if x>=0 or y>=0:
    print("At least one number is positive")
else:
    print("Bot numbers are negative")