# 8.	Paul is 21 and Annie 18. Write a program that checks that both are adults.

paul = int(21)
annie = int(18)

adult = int(input("Adult age is: "))

if paul >= adult and annie >= adult:
    print("Both are adults")
else:
    print("At least one guy is underaged")