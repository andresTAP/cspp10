import random




def get_round():
    rounds = int(input("how many rounds would you like to play from 1 to 9 "))
    return rounds

def get_p1_move():
    p1_move = input("Would you like to play Rock, Paper or Scissors ")
    if p1_move.lower() == "rock":
        return "Rock"
    elif p1_move.lower() == "paper":
        return "Paper"
    elif p1_move.lower() == "scissors":
        return "Scissors"
    else:
        return "WRONG "

def get_comp_move():
    comp_move = random.randint(1,3)
    if comp_move == 1:
        return "Rock"
    elif comp_move == 2:
        return "Paper"
    elif comp_move == 3:
        return "Scissors"

def get_winner(p1_move,comp_move):
    if p1_move == comp_move:
        return "Its A TIE! "
    elif comp_move == "paper " and p1_move == "rock ":
        return "Computer Wins!"
    elif p1_move == "rock " and comp_move == "paper ":
        return "Player Wins!"
    elif p1_move == "paper " and comp_move == " scissors ":
        return "Player Wins!"
    elif comp_move == " scissors " and p1_move == "paper":
        return "Computer Wins!"
    elif p1_move == " rock " and comp_move == "scissors ":
        return "Player Wins!"
    elif comp_move == "rock " and p1_move == "scissors ":
        return " Computer Wins!"
 

#def get_round():
   # rounds = int(input("how many rounds would you like to play from 1 to 9 "))
    #return rounds

print(get_comp_move())
print(get_round())
print(get_p1_move())

print(get_winner("paper","rock "))
