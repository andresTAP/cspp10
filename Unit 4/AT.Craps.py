import random
The_House = 100
player_amount = 100


print("Lets Play some Craps!")
print("----------------------")

def phase_1():
    if player_amount < 0:
        return " You are broke!"
    elif player_amount > 0:
        return input(int(" How much would you like to bet?: "))

def rolling_dices():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("Rolled 2 dice: {} {}".format(dice1,dice2))
    return dice_sum

def phase_2(sum_of_dice):
    if sum_of_dice == (7): 
        return "Player wins!"
    elif sum_of_dice == (2,3,12): 
       return "House Wins!"
    else: 
        return "point"

def phase_3():    
    
    
#rolling_dices() 