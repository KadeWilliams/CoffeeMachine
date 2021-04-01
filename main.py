import sys
from information import resources, MENU

profit = 0


def report():
    """Acquire the current status of the machine's resources"""
    water = resources['water']
    coffee = resources['coffee']
    milk = resources['milk']
    return f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: ${profit}"


def get_drink():
    """Get user's desired choice, generate the report, or exit the machine"""
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'report':
        print(report())
        return False
    elif choice in MENU.keys():
        return choice
    elif choice == 'off':
        sys.exit()
    else:
        print('Invalid entry! Please try again.')


def check_resources(drink_ingredients):
    """Check the current resources of the machine against the required ingredients"""
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry, there's not enough {item}.")
            return False
    return True


def get_coins():
    """Get change from user to pay for drink"""
    total = int(input("How many quarters?: ")) * .25
    total += int(input("How many dimes?: ")) * .1
    total += int(input("How many nickels?: ")) * .05
    total += int(input("How many pennies?: ")) * .01
    return total


def enough_coins(drink):
    """Check to see if the payment was successful and update profit"""
    wallet = get_coins()
    if wallet >= MENU[drink]['cost']:
        change = wallet - MENU[drink]['cost']
        global profit
        profit += MENU[drink]['cost']
        print(f"Here's your change, {round(change, 2)}.")
        return True
    print("Sorry, not enough money. Money refunded.")
    return False


def make_coffee(drink, ingredients):
    """Reduce the amount of resources based on ingredient required"""
    for item in ingredients:
        resources[item] -= ingredients[item]
    return f"Here's your {drink}. Enjoy"


while True:
    drink = get_drink()
    if drink:
        ingredients = MENU[drink]['ingredients']
        if check_resources(ingredients):
            if enough_coins(drink):
                print(make_coffee(drink, ingredients))
