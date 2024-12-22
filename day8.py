alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            if new_position > 25:
                proper_position = new_position % 26
            else:
                proper_position = new_position
            cipher_text += alphabet[proper_position]
        else:
            cipher_text += letter
    print(f"The encoded text is {cipher_text}")


def decrypt(plain_text, shift_amount):
    decrypted_message = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            old_position  = position - shift_amount
            if old_position < -26:
                old_proper_position = old_position % 26
            else:
                old_proper_position = old_position
            decrypted_message += alphabet[old_proper_position]
        else:
            decrypted_message += letter
    print(f"The decoded text is {decrypted_message}")



def ceaser(choice):
    if choice == "encode":
        encrypt(plain_text=text, shift_amount=shift)

    elif choice == "decode":
        decrypt(plain_text=text, shift_amount=shift)
    else:
        print("Invalid input!")
        
ceaser(choice=direction)
final_question = input("Do you wanna encode or decode again? If yes, yes. Otherwise, type no!\n").lower()

while final_question == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(choice=direction)
    final_question = input("Do you wanna encode or decode again? If yes, yes. Otherwise, type no!\n").lower()








