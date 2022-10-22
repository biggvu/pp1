import math

a = (int(input("a= ")))
b = (int(input("b= ")))
c = (int(input("c= ")))
s = (a+b+c)/2

heron_f = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(heron_f)