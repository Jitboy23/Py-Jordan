#Band Name Generator Project
#I made sure the input curser showed up on a new line by adding a \n to the very end of the string
Band1_name = (input("Welcome to the Band Name Generator!\nWhat's the name of the city you grew up in?\n"))

Band2_name = (input("What's your favorite zoo animal to look at?\n"))

#I used " " to create  space inetween my variables that I'm adding together
Band3_name = ((Band1_name) + " " + (Band2_name))

print("Your name could be the " + (Band3_name))
