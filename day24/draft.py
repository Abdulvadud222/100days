# with open("my_file.txt") as file: ###this feature allows the user to open files without having to close it. Now the txt
#     ###file is equal to the variable "file"
#     contents = file.read() ### this turns everything in file into string and assigns them to the variable contents
#     print(contents)

with open("../../Desktop/my_file.txt", mode="a") as file: ###if mode is "w", we overwrite the text. if it is "a", we append
    file.write("New text")
    file.write(" has been added!")
    file.write("New text")
    file.write(" has been added!")
    file.write("\n Yo-Yo")



