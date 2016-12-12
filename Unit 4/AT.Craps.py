import random
player_amount = 100


print("Lets Play some Craps!")
print("----------------------")

def player_regulations():
    if player_amount < 0:
        return " You are broke!"
    elif player_amount > 0:
        return input(int(" How much would you like to bet?: "))

def bet_amount(player_bet):
    if player_bet 

def phase_1():
    if dice_sum == (7) and (11):
        return player_bet 

def rolling_dices():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("Rolled 2 dice: {} {}".format(dice1,dice2))
    return dice_sum

def phase_2(sum_of_dice):
    if sum_of_dice == (7) or (11): 
        return "Player wins!" +1
    elif sum_of_dice == (2) or (3) and (12): 
       return "House Wins!" +1
    else: 
        return "point"

def phase_3():
    if dice_sum == 
    


#player_regulations()
#phase_1()
#rolling_dices()
#phase_2()
