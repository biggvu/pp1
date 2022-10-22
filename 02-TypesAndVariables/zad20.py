from cmath import inf
import random

max = (int(input("Maximum roll: ")))

k1 = random.randrange(1,max)
k2 = random.randrange(1,max)
k3 = random.randrange(1,max)

print(f"Sum of rolls: {k1+k2+k3}")
