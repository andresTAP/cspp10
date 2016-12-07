import random
player_amount = 100


print("Lets Play some Craps!")





#function name: Rolling dice
#purpose: generating two dice rolls and pritns it out, and returns the sum
#arguements:none
#returns: teh sum of two dice
def rolling_dices():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("Rolled 2 dice: {} {}".format(dice1,dice2))
    return dice_sum

rolling_dices()