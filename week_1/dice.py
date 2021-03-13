dice1 = 0
dice2 = 0
diceSum = 0
rolls = 0
target = 7
targetHit = False
print("This program rolls two 6-sided dice until their sum is a given target.")

while targetHit == False:
    dice1 = int(input("Please enete dice1: "))
    dice2 = int(input("Please enete dice2: "))
    diceSum = dice1 + dice2
    rolls = rolls + 1
    print(dice1)
    print(dice2)
    print(diceSum)
    if diceSum == target:
        targetHit = True
        print("You Got It!!")

    else:
        print("Keep Going!!")

print("Game is over!")
