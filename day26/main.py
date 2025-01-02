# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num**2 for num in numbers]
# print(squared_numbers)

# result = [num for num in numbers if num % 2 == 0]
# print(result)



###if you want to use this code, add nums to the first lines in file1 and file2
# import pandas
# file1_csv = pandas.read_csv("file1.txt")
# file1_list = file1_csv["nums"].to_list()
#
# file2_csv = pandas.read_csv("file2.txt")
# file2_list = file2_csv["nums"].to_list()
#
# result = [num for num in file1_list if num in file2_list]
# print(result)

# with open("file1.txt") as file1:
#     file1_list = file1.readlines()
#
# with open("file2.txt") as file2:
#     file2_list = file2.readlines()
#
# result = [num.strip("\n") for num in file1_list if num in file2_list]
# print(result)

# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie",]
# student_scores = {name:random.randint(1, 100) for name in names}


# passed_students = {student: score for student, score in student_scores.items() if score >= 60} ##I must use .items() to loop through a dict
#
# print(passed_students)


# sentence = "What is the Airspeed Velocity of an Unladen Swallow"
# sentence_list = sentence.split()
# result = {word: len(word) for word in sentence_list}
#
# print(result)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# weather_f = {day: round((degree*1.8) + 32, 1) for (day, degree) in weather_c.items()}
# print(weather_f)


import pandas

# student_dict = {
#     "student": ["Angela", "James", "Lily",],
#     "score": [56, 76, 98,],
# }
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# for (index, row) in student_data_frame.iterrows():
#     print(index)
#     print(row.student)
#     print(row.score)


alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for (index, row) in alphabet.iterrows()}

user_word = input("Enter a word: ").upper()

result = [alphabet_dict[letter] for letter in user_word]

print(result)
