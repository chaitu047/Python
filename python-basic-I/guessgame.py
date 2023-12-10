import random

genRandInt = random.randint(0,9)

inputInt = int(input("Enter input"))

if genRandInt==inputInt:
    print("Win")
else:
    print("lost")