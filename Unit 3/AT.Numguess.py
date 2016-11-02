import random
num = random.randint(1,101)
guess_machine = int(input("Enter a guess between 1-100: "))

while guess_machine != num:
    
    if guess_machine < num:
        print("Too Low")
        guess_machine = int(input("Guess again: "))
        
    elif guess_machine > num:
        print("Too High")
        guess_machine = int(input("Guess again: "))
        
    elif guess_machine == num:
        print("You got it! It was indeed {}".format(num)) 
    
    
    