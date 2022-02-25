height = (input("Enter your height. \nFeet: ") + (input("\nInches: ")))
#print(height)
#Feet = 5
#Inches = 9
#print(len(height))
#len was 2
Feet = (int(height[0]))
#print(Feet)
#5

Inches = (int(height[1]))
#print(Inches)
#9

Total_Inches = ((Feet * 12) + Inches)

weight = (input("\nEenter your weight in pounds: "))
#print(weight)
#Weight was 145lbs
weight2 = (int(weight))

BMI = ((weight2 * 703) / Total_Inches**2)

Total_BMI = (int(BMI))
print("\nYour total BMI is: " + str(Total_BMI))