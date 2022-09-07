import random
from Data_Celeb import data

from Da_art import logo, vs

#A function to clear the screen
def clear():
    """This function will give you 50 new line characters which is enough to clear off the screen"""
    print('\n' * 50)

#A function to keep track of the data of each celebrity
def celeb_data(celeb):
    """Takes the account data and returns the printable format."""
    name = celeb['name']   #print(name)
    description = celeb['description']  #print(description)
    country = celeb['country']   #print(country)
    return(f"{name}, a {description} from {country}.")

#A function to check the answer. This function will only work if the answer is right
def check_answer(user_guess, follower1, follower2):
    """Use if statement to check if user is correct."""
    if follower1 > follower2:
        return user_guess == "a" #The function will only return if the user guess was actually  "a". If not, then it won't return
    else:
        return user_guess == "b" #The function will only return if the user guess was actually  "b". If not, then it won't return

#display art
print(logo)
score = 0

#While loop flag
game_should_continue = True
celeb2 = random.choice(data)

#Make the game repeatable.
while game_should_continue == True:

    #Make sure that account at position B becomes the next account at position A.
    celeb1 = celeb2
    celeb2 = random.choice(data)

    while celeb1 == celeb2:
        celeb2 = random.choice(data)

    print(f"Compare A: {celeb_data(celeb1)}.") #Calling the celeb_data functon and using celeb1 as the value
    print(vs)
    print(f"Against B: {celeb_data(celeb2)} ") #Calling the celeb_data functon and using celeb2 as the value

    guess = input("Who has more instagram followers? Type 'A' or 'B': " ).lower()

        #Grapping the follower count for each account
    followers1 = int(celeb1['follower_count'])
    #print(followers1)
    followers2 = int(celeb2['follower_count'])
    #print(followers2)

    is_correct = check_answer(guess, followers1, followers2)
    clear()
    print(logo)

    if is_correct: 
        score += 1 #This is the same as putting -  score = score + 1
        print(f"You're right! Current score: {score}")
    else:
        clear()
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False
