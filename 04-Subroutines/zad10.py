#10.	Define a function read_number() that returns an integer number entered from the keyboard. 
#The function should print a text prompting user to enter the number 'Enter a number: '. Then use the function to read two numbers from the keyboard. Display their sum.

def read_number():
    number = int(input("Enter a number: "))
    return number

x = read_number()
y = read_number()

print(x+y)
