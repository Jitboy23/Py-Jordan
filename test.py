#!/usr/bn/pyhton3

print ("Welcome to the Test!")

user_choice = input("Do you want to proceed with the Test?[Y/N]")

if user_choice == "Y":
	user_name = input("Enter your user name: ")
	excitement_level = input("Enter your excitement level for the test: ")
	print ("Congrats " + user_name + " , you have the exitement level of " + excitement_level + "!")
else: 
	print ("Have a good day!")	

