#Auction House Dictionary Project

#I created a function to find the highest bidder with the value of the function being the bidding dictionary
def find_highest_bidder(bidding_dictionary):
    highest_bid = 0 #We start out with a zero so each time the for loop is run, the 0 can turn into the value bid number
    winner = "" #This string is for the print statement that'll have the name of the highest bidder(the key in the dictionary)
    # bidding_dictionary = {name: 123, name: 300}
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder] #This is how you'll loop through the bid numbers(values) stored in the keys of the bid_dic1
        if bid_amount > highest_bid:
            highest_bid = bid_amount 
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
#Once the for loop loops throug all the bids, the highest bid number should be higher than the other numbers 
#looped after the highest bid variables changed to those numbers


bid_dic1 = {} #bid_dic1 = bidding dictionary
game = True
while game == True:
    print("Welcome to the auction house!")
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bid_dic1[name] = bid
    question = input("Are there any other bidder? Y/N?: ").lower()
    if question == "n":
        game = False
        find_highest_bidder(bid_dic1)
        print(bid_dic1)
#Ouput:
#Are there any other bidder? Y/N?: y
#Welcome to the auction house!
#What is your name?: Aaron
#What's your bid?: $420
#Are there any other bidder? Y/N?: y
#Welcome to the auction house!
#What is your name?: Maisha
#What's your bid?: $75
#Are there any other bidder? Y/N?: n
#The winner is Aaron with a bid of $420