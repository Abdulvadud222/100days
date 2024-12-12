# # Challenge 1: adding the digits of the number
# numst  = input("Please, input the number to be processed: ") #get the input as string
# nums = list(numst) #turn the string into a list
# result = 0
# for num in nums:
#     num  = int(num) # turn the list item into an integer so that we can add
#     result += num

# print(f"The processed number is {result}")











# # Challenge 2: calculating BMI

# height = float(input("Please, input your height in meters(with a point before cm part): "))
# weight = float(input("PLease, input your weight in kilos: "))
# bmi = weight/(height ** 2)
# bmi = round(bmi, 1)
# print(f"Your BMI is {bmi}.")

# if bmi < 18.5:
#     print("Dude, you are so thin. Eat mooore!!!")
# elif 18.5 <= bmi <24.9:
#     print("You have a normal weight")
# elif 25.0 <= bmi < 29.9:
#     print("You are overweight")
# elif bmi >= 30.0:
#     print("You are obese(")


# # Challenge 3: calculating how many weeks a person has if they are lucky to live 90 years

# age = int(input("Please, input your age: "))
# rlife = 90 - age # rlife stands for how many years they have
# days = round(rlife * 365.25)
# weeks = rlife * 52
# months = rlife * 12
# message = f"You have {days} days, {weeks} weeks, and {months} months left."
# print(message)


# # Challenge 4: Tip calculator
# print("Welcome to the tip calculator.")
# bill = float(input("What was the total bill?  "))
# tp = float(input("What percentage tip would you like to give? ")) # tp stands for the tip percentage
# people = float(input("How many people to split the bill? "))
# fbill = bill + (bill * (tp/100))
# result = fbill/people
# resultr = "{:.2f}".format(result) # reultr stands for rounded result
# print(f"Each person should pay: ${resultr}")






























 














































































