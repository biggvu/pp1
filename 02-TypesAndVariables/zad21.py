import random

pc_k = random.randrange(1,6)
guess = (int(input("Try to guess the number (1-6): ")))

print(pc_k==guess)
print(f"It was {pc_k}")