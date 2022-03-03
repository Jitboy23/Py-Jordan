#Day 2 Project: Tip Calculator
Bill = (float(input("Welcome to the tip calculator. \nWhat was the total bill? $")))

Tip = (int(input("What percentage tip would you like to give? 10, 12, or 15? ")))

People = (int(input("How many people will split te bill? ")))

#To find out what the percentage tip would be you want to divide the tip from 100. For example: 10/100 = 0.10
#Then multiply 0.10 by the bill total. Example: 0.10 * 124.43 = 12.443
#Then you want to add the the sum you got to the total bill again. 
#Example of the full problem: (10/100)* 124.43 + 124.43

Bill_with_tip = ((Tip / 100) * Bill + Bill)
#To split the total bill amongst people, you need to divide the total bill by the number of people

Total = (Bill_with_tip / People)
#In order to get your answer to show 4 digets like a normal price would($12.23), you need to round the float decimal two places
#An example: (round(12.3432),2)
#This would give you: 12.34 instead of 12.3432
result = (round(Total,2))

print(f"Each person should pay: ${result}")





