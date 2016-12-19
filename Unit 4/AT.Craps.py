import random
bank_amount = 100


print("Lets Play some Craps!")
print("----------------------")

def player_regulations(bank_amount):
    if bank_amount < 0:
        return " You are broke!"
    elif bank_amount > 0:
        return input(int(" How much would you like to bet?: "))
 

def phase1(bank_amount):
    bet = int(input("How much do you want to bet: "))
    while True:
        if bet < 0:
            print("No negative numbers")
            
        elif bet <= bank_amount:
            return bet
            
        elif bet > bank_amount:
            print("You don't have that kind of money")
            bet = int(input("Bank Acc: 100, How much do you want to bet: "))

    

def rolling_dices():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("Rolled 2 dice: {} {}".format(dice1,dice2))
    return dice_sum


def phase2(sum_of_dice,point_number):
    if sum_of_dice == (7) or (11): 
        return "Player wins!" +1
    elif sum_of_dice == (2) or (3) and (12): 
       return "House Wins!"
    elif point_number == (1) or (4) or (5) or (6) or (8) or (9) or (10):
        return("Point number:{} ".format(point_number))


def phase3(dice_sum):
    new_dice1 = random.randint(1,6)
    new_dice2 = random.randint(1,6)
    new_dice_sum = new_dice1 + new_dice2 
    if new_dice_sum != 7 or  new_dice_sum != dice_sum:
        while new_dice_sum != 7 or  new_dice_sum != dice_sum:
            print("Dice 1: {} Dice 2: {}".format(new_dice1, new_dice2))
            break
        
    elif new_dice_sum == 7 or new_dice_sum == dice_sum:
        print("You Win")    

def craps(bet,get_bank,rolling_dices,rolling2dices):
    bank_amount == 100
    bet = get_bet(bank_amount)
    rolling_dices = rolling2_dices 
    
    while bank_amount > 0:
        return 





craps()
phase1(bank_amount)
player_regulations(bank_amount)
rolling_dices()
#phase2()
#phase3()
