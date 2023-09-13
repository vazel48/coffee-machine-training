MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money_inside = 0


def is_enough_resources(order_ingredients):
    """Returns True when order can be made, False if ingredients are not enough."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item} :(")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]


is_working = True
while is_working == True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_working = False
    elif choice == "report":
        print(f'Water: {resources["water"]} ml')
        print(f'Milk: {resources["milk"]} ml')
        print(f'Coffee: {resources["coffee"]} g')
        print(f'Money: ${money_inside}')
    else:
        drink = MENU[choice]
        if is_enough_resources(drink["ingredients"]):
            user_payment = process_coins()
            if user_payment >= drink["cost"]:
                print(f"Here is your {choice}. Enjoy! 🎂")
                money_inside += drink["cost"]
                change = round(user_payment - drink["cost"], 2)
                print(f"And here is ${change} dollars your change.")
                make_coffee(choice, drink["ingredients"])
            else:
                print("Sorry that's not enough money. Money refunded.")
