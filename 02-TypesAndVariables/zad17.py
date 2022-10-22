height_cm = (int(input("Your height in cm: ")))
height_ft = height_cm*0.0328084
height_in = (height_ft - int(height_ft))*12
print(f"I am {height_cm} cm tall, i.e. {int(height_ft)} feet and {int(height_in)} inches.")