# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("/Users/microsoftn/Downloads/Mail Merge Project Start/Input/Letters/starting_letter.txt") as the_letter:
    lines = the_letter.readlines()  ### this reads the file and turns into a list

with open("/Users/microsoftn/Downloads/Mail Merge Project Start/Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()  ### this reads the file and turns into a list

for name in names:
    stripped_name = name.strip("\n")  ###we are stripping "\n" part.
    lines[0] = f"Dear {stripped_name},\n"  ###we are changing line[0]
    with open(f"/Users/microsoftn/Downloads/Mail Merge Project Start/Output/ReadyToSend/email_for_{stripped_name}",
              mode="w") as ready_emails:
        ready_emails.writelines(lines)  ###this writes in the file.


