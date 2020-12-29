import random

def dice1():
    return(random.randint(1,6))
def dice2():
    return(random.randint(4,6))

print("Type roll to roll dice and quit to quit")
print("Type rollspecialdice to roll biased dice")

i = 0
while i == 0 :
    
    value = input()
    if value == "roll":
        print(dice1())
    if value == "rollspecialdice":
        print(dice2())
    if value == "quit":
        break

