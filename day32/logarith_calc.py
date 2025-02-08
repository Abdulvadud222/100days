
import math
print("Welcome to a logarithm calculator!\n\nDon't write 'log'.\n\nInput 'x' for the value you are looking for!")
further_calculations = True
while further_calculations:
    base = input("Input the base(for 'ln' input 'e'): ").lower()
    argument = input("Input the argument: ").lower()
    exponent = input("Input the exponent: ").lower()
    if base == "e":
        base  = 2.72
    else:
        pass
    if base == "x":
        argument_int = int(argument)
        exponent_int = int(exponent)
        base = round(argument_int ** (1/exponent_int), 2)
        print(f"The base is {base}")
    elif argument == "x":
        base_int = int(base)
        exponent_int = int(exponent)
        argument = round(base_int ** exponent_int, 2)
        print(f"The argument is {argument}")
    elif exponent == "x":
        base_int = int(base)
        argument_int = int(argument)
        exponent = round(math.log(argument_int, base_int), 2)
        print(f"The exponent {exponent}")
    else:
        print("Invalid input!")

    final_question = input("For further calculations type 'y', for quitting type 'n': ").lower()
    if final_question == 'y':
        further_calculations = True
    elif final_question == 'n':
        further_calculations = False
    else:
        print("Invalid command!\nExiting...")
        further_calculations = False






