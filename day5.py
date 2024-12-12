# student_heights = input("Input student heights in cm without a comma but with a space: ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = float(student_heights[n])

# overall_height = 0
# for i in student_heights:
#     overall_height += i


# number_of_students = 0
# for n in student_heights:
#     number_of_students += 1

# average = round(overall_height/number_of_students, 2)

# print(f"The average height in the class is {average}cm")





# student_scores = input("Input a list of student scores with a space: ").split() #this split() method turns the string into a list

# for n in range(0, len(student_scores)):
#     student_scores[n] = float(student_scores[n])
# highest = 0
# for score in student_scores:
#     if score >= highest:
#         highest = score
# print(f"The highest score in the class is: {highest}")

# #for loop with range
# for number in range(1, 10):
#     print(number) #it will print from 1 to 9 but not 10 as range doesn't include the last item
# for num in range(1, 10, 2):
#     print(num) #it will print from 1 to 9 by taking a two step: that is, 1 3 5 7 9

# total = 0
# for digit in range(0, 101, 2):
#     total += digit
# print(total)

# #fizzbuzz
# for numb in range(1, 101):
#     if numb % 15 == 0:
#         numb = "FizzBuzz"
#     elif numb % 5 == 0:
#         numb = "Buzz"
#     elif numb % 3 == 0:
#         numb = "Fizz"
#     print(numb)

# ###easy version
# import random
# import string

# print("Welcome to the PyPassword Generator!")
# letter_length = int(input("How many letters would you like in your password: "))
# symbol_length = int(input("How many symbols would you like: "))
# number_length = int(input("How many numbers would you like: "))


# letters = list(string.ascii_lowercase + string.ascii_uppercase)
# symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
# numbers = ["0", "1", "2", "3", "4", "5", "6," "7", "8", "9"]

# rand_letters = random.choices(letters, k = letter_length) #now i get letter_length times random letters from letters by using this "k =" 
# rand_symbols = random.choices(symbols, k = symbol_length)
# rand_numbers = random.choices(numbers, k = number_length)

# rand_letters_string = "".join(rand_letters)
# rand_symbols_string = "".join(rand_symbols)
# rand_numbers_string = "".join(rand_numbers)
# password = rand_letters_string + rand_symbols_string + rand_numbers_string

# print(f"The generated password is {password}")


# ###harder one
# import random
# import string

# print("Welcome to the PyPassword Generator!")
# letter_length = int(input("How many letters would you like in your password: "))
# symbol_length = int(input("How many symbols would you like: "))
# number_length = int(input("How many numbers would you like: "))


# letters = list(string.ascii_lowercase + string.ascii_uppercase)
# symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
# numbers = ["0", "1", "2", "3", "4", "5", "6," "7", "8", "9"]

# rand_letters = random.choices(letters, k = letter_length) ###now i get letter_length times random letters from letters by using this "k =" 
# rand_symbols = random.choices(symbols, k = symbol_length)
# rand_numbers = random.choices(numbers, k = number_length)

# password_list = rand_letters + rand_symbols + rand_numbers ###this puts all three lists into one list

# random.shuffle(password_list) ###this shuffles the list
# passwordhard = "".join(password_list)
# print(f"The generated password is: {passwordhard}")



