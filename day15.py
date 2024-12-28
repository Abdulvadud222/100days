

def current_resource():
    resource = {
        "Water": 300,
        "Milk": 200,
        "Coffee": 100,
        "Money": 0
    }
    water = resource["Water"]
    milk = resource["Milk"]
    coffee = resource["Coffee"]
    money = resource["Money"]
    return water, milk, coffee, money, resource

resource_tuple = current_resource()
resource_list = list(resource_tuple)
resource_dic = resource_list[4]
resource_water = resource_dic["Water"]
resource_milk = resource_dic["Milk"]
resource_coffee = resource_dic["Coffee"]
resource_money = resource_dic["Money"]
resource_list[0] = resource_dic["Water"]
resource_list[1] = resource_dic["Milk"]
resource_list[2] = resource_dic["Coffee"]
resource_list[3] = resource_dic["Money"]
def sync_resource_list():
    resource_list[0] = resource_dic["Water"]
    resource_list[1] = resource_dic["Milk"]
    resource_list[2] = resource_dic["Coffee"]
    resource_list[3] = resource_dic["Money"]


def expresso():
    expresso_water = 50
    expresso_coffee = 18
    cost = 2.5
    return expresso_water, expresso_coffee, cost

expresso_list = expresso()


def latte():
    latte_water = 200
    latte_milk = 150
    latte_coffee = 24
    cost = 4
    return latte_water, latte_milk, latte_coffee, cost

latte_list = latte()


def cappuccino():
    cappuccino_water = 250
    cappuccino_milk = 100
    cappuccino_coffee = 24
    cost = 4
    return cappuccino_water, cappuccino_milk, cappuccino_coffee, cost

cappuccino_list = cappuccino()

def comparer(prompt, resource_list, expresso_list, latte_list, cappuccino_list):
    if prompt == "e":
        if resource_list[0] >= expresso_list[0] and resource_list[2] >= expresso_list[1]:
            return "enough"
        else:
            return 0
    elif prompt == "l":
        if resource_list[0] >= latte_list[0] and resource_list[1] >= latte_list[1] and resource_list[2] >= latte_list[2]:
            return "enough"
        else:
            return 0
    elif prompt == "c":
        if resource_list[0] >= cappuccino_list[0] and resource_list[1] >= cappuccino_list[1] and resource_list[2] >= cappuccino_list[2]:
            return "enough"
        else:
            return 0



print("The user manual:\n1) Choose the type\n2) Input the coins\n3) Type 'r' to see the available resource\n4) If you want to turn the machine off, type 'off'")
prompt = input("What would you like? Type 'e' for expresso, 'l' for latte, and 'c' for cappuccino: ").lower()
if prompt == "off":
    turn_off = True
elif prompt == "r":
    turn_off = False
    print(resource_list[4])
    prompt = input("What would you like? Type 'e' for expresso, 'l' for latte, and 'c' for cappuccino: ").lower()
else:
    turn_off = False


def insert_coin():
    print("The machine works with only coins!\nPennies 1 cent, Nickels 5 cents, Dimes 10 cents, and Quarters 25 cents!")
    pennies = int(input("How many pennies: "))
    nickels = int(input("How many nickles: "))
    dimes = int(input("How many dimes: "))
    quarters = int(input("How many quarters: "))
    overall_money = (pennies + 5*nickels + 10*dimes + 25*quarters)/100
    return overall_money





while not turn_off:
    resource_check = comparer(prompt, resource_list, expresso_list, latte_list, cappuccino_list)
    if  resource_check == "enough":
        if prompt == "e":
            print(f"Expresso costs ${expresso_list[2]}")

            your_money = insert_coin()
            if your_money >= expresso_list[2]:
                refund = round((your_money - expresso_list[2]),2)
                resource_dic["Water"] -= expresso_list[0]
                resource_dic["Coffee"] -= expresso_list[1]
                resource_dic["Money"] += 2.5
                sync_resource_list()
                print("Here is your coffee ☕️. Enjoy it!")
                print(f"Here is your refunded money. ${refund}")
            else:
                print("Not enough coins. Money is refunded")
                print(f"Here is your refunded money. ${your_money}")
        elif prompt == "l":
            print(f"Latte costs ${latte_list[3]}")

            your_money = insert_coin()
            if your_money >= latte_list[3]:
                refund = round((your_money - latte_list[3]),2)
                resource_dic["Water"] -= latte_list[0]
                resource_dic["Milk"] -= latte_list[1]
                resource_dic["Coffee"] -= latte_list[2]
                resource_dic["Money"] += 4
                sync_resource_list()
                print("Here is your coffee ☕️. Enjoy it!")
                print(f"Here is your refunded money. ${refund}")
            else:
                print("Not enough coins. Money is refunded")
                print(f"Here is your refunded money. ${your_money}")
        elif prompt == "c":
            print(f"Cappuccino costs ${cappuccino_list[3]}")

            your_money = insert_coin()
            if your_money >= cappuccino_list[3]:
                refund = round((your_money - cappuccino_list[3]),2)
                resource_dic["Water"] -= cappuccino_list[0]
                resource_dic["Milk"] -= cappuccino_list[1]
                resource_dic["Coffee"] -= cappuccino_list[2]
                resource_dic["Money"] += 4
                sync_resource_list()
                print("Here is your coffee ☕️. Enjoy it!")
                print(f"Here is your refunded money. ${refund}")
            else:
                print("Not enough coins. Money is refunded")
                print(f"Here is your refunded money. ${your_money}")
    else:
        print("Not enough resources! Exiting...")
        break
    print("The user manual:\n1) Choose the type\n2) Input the coins\n3) Type 'r' to see the available resource\n4) If you want to turn the machine off, type 'off'")
    prompt = input("What would you like? Type 'e' for expresso, 'l' for latte, and 'c' for cappuccino: ").lower()
    if prompt == "off":
        turn_off = True
    elif prompt == "r":
        print(resource_list[4])
        prompt = input("What would you like? Type 'e' for expresso, 'l' for latte, and 'c' for cappuccino: ").lower()
        sync_resource_list()
    else:
        turn_off = False





