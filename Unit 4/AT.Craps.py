import random
bank_amount = 100


print("Lets Play some Craps!")
print("----------------------")

def player_regulations():
    if player_amount < 0:
        return " You are broke!"
    elif player_amount > 0:
        return input(int(" How much would you like to bet?: "))

def bet_amount(bank_amount):
    bet = int(input("How much do you want to bet: "))
    while True:
        if bet < 0:
            print("No negative numbers")
            
        elif bet <= bank_amount:
            return bet
            
        elif bet > bank_amount:
            print("You don't have that kind of money")
            bet = int(input("Bank Acc: 100, How much do you want to bet: "))

def phase_1():
    if dice_sum == (7) and (11):
        return "You have won! "

def rolling_dices():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print("Rolled 2 dice: {} {}".format(dice1,dice2))
    return dice_sum

def phase_2(sum_of_dice):
    if sum_of_dice == (7) or (11): 
        return "Player wins!" +1
    elif sum_of_dice == (2) or (3) and (12): 
       return "House Wins!" +1
    else: 
        return "point"




def phase3():
    if dice_sum

#player_regulations()
#phase_1()
#rolling_dices()
#phase_2()
