
# f_name = input("What's your first name?: ").lower()
# l_name = input("What's your last name?: ").lower()


# def format_name(first_name, last_name):
#     if first_name.strip() == "" or last_name.strip() == "":
#         return "You didn't provide valid inputs!"
#     formatted_first_name = first_name.title()
#     formatted_last_name = last_name.title()
#     full_name = f"Your full name is {formatted_first_name} {formatted_last_name}"
#     return full_name
# print(format_name(first_name=f_name, last_name=l_name)) 


# def is_leap(year):
#     """Return whether the year is leap or not"""
#     if year % 400 == 0:
#         return True
#     elif year % 4 == 0  and year % 100 != 0:
#         return True
#     else:
#         return False

# def days_in_month(year, month):
#     """Return the number of days in a month"""
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) == True:
#         month_days[1] = 29
#     return month_days[month - 1]
    



# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(f"There are {days} days in that month!")


###final project: calculator
#
#
#
# def add(n1, n2):
#     """Returns the addition"""
#     return n1 + n2
#
# def subtract(n1, n2):
#     """Return the subtraction"""
#     return n1 - n2
#
# def multiply(n1, n2):
#     """Returns multiplication"""
#     return n1 * n2
#
# def divide(n1, n2):
#     """Return Division"""
#     return n1 / n2
#
# operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide,
# }
# def calculator():
#     num1 = float(input("What's the first number: "))
#     for symbol in operations:
#         print(symbol)
#
#     should_continue = True
#
#     while should_continue:
#         choice = input("Pick an operation: ")
#         if choice not in ["+", "-", "*", "/"]:
#             print("Invalid operation symbol! Please pick from +, -, *, /.\n"
#                   "Exiting...")
#             break
#         num2 = float(input("What's the next number: "))
#         operation = operations[choice]
#         answer = operation(num1, num2)
#         print(f"{num1} {choice} {num2} = {answer}")
#         again = input(f"If you want to continue with {answer}, type y. Otherwise type n: ").lower()
#         if again in ["y"]:
#             should_continue = True
#             num1 = answer
#         else:
#             should_continue = False
#             calculator()
# calculator()
