#Meant to scramble the letters in the word or phrase when code is complete and functional
import random

#Purpose is to recognize the user's input
#This will scramble the word the user typed 
#Trying to make this function without the use of scramble()will be my goal
def scramble_word():
    user_input = input("Enter a language: ")
    some_word = list(user_input)
    random.shuffle(some_word)
    print(some_word)
    
    
    
    
    
    
    
    
    
#Instead of just a word this will scramble the letters of every word in an entire sentence
#The function scramble.word will still be neccesary, and will be towards scrambiling an entire sentence 
#With the exception of the first and last letter of the word




#def scramble_phrase():
     
scramble_word()     