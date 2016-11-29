import random




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

def get_round():
    rounds = int(input("how many rounds would you like to play from 1 to 9 "))
    return rounds

def get_winner(p1_move,comp_move):
    if p1_move == comp_move:
        return "Tie"
    elif comp_move == "paper " and p1_move == "rock ":
        return "Computer"
    elif p1_move == "rock " and comp_move == "paper ":
        return "Player"
    elif p1_move == "paper " and comp_move == " scissors ":
        return "Player"
    elif comp_move == " scissors" and p1_move == "paper":
        return "Computer"
    elif p1_move == " rock " and comp_move == "scissors ":
        return "Player"
    elif comp_move == "rock " and p1_move == "scissors ":
        return " Computer"

def get_full_move(short_move):
    if short_move == "r":
        return "Rock"
    elif short_move == 'p':
        return "Paper"
    elif short_move == 's':
        return "Scissors"

def print_score(pscore, cscore, ties):
    return("Player Wins: {}/n Computer Wins: {}/n Ties: {}")

def rps():
    rounds = get_round()
    
    pscore = 0
    cscore = 0
    ties = 0
    
    for x in range(rounds):
        p1move = get_p1_move()
        compmove = get_comp_move()
    
        print("Player chose {}".format( get_full_move(p1move)))
        print("The computer chose {}".format( get_full_move(compmove) ) )
    
        winner = get_winner(p1move,compmove)
        if winner == "Player":
            print("Player1 won")
            pscore = pscore + 1
        
        elif winner == "Computer":
            print("The Computer won")
            cscore = cscore + 1
            
        elif winner == "Tie":
            print("It's a tie")
            ties = ties + 1
        print(print_score(pscore, cscore, ties))
        print("-------------------") 





print(get_round())
print(get_p1_move())
print(get_comp_move())
print(get_winner(get_p1_move,get_comp_move))
print(rps)

