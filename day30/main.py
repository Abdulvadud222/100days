# with open("data.txt") as data:
#     data.read()

# try:
#     file = open("a_file.txt")
#     dict = {"key": "value"}
#     print(dict[""])
# except FileNotFoundError:
#     with open("a_file.txt", "w") as file:
#         file.write("writing")
# except KeyError as error_message:
#     print(f"{error_message} does not exist!")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("made up error")


# fruits = ["Apple", "Pear", "Orange"]
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
#
# make_pie(2)


# facebook_posts = [
#     {"Likes": 21, "Comments": 2},
#     {"Likes": 13, "Comments": 2, "Shares": 1},
#     {"Likes": 33, "Comments": 8, "Shares": 3},
#     {"Comments": 4, "Shares": 2},
#     {"Comments": 1, "Shares": 1},
#     {"Likes": 19, "Comments": 3},
# ]
#
# total_likes = 0
#
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post["Likes"]
#     except KeyError:
#         pass ###because I pass, it ignores KeyError
#
# print(total_likes)





