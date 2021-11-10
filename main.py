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
money = 100
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#TODO:1.Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is dispensed.
# The prompt should show again to serve the next customer.



def make_coffe(ingredients, order):
    global resources
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"You ordered {order}")

def money_work(cash, order):
    global MENU
    global money
    print(f"You inserted {cash}$")

    win = float(cash) - float(MENU[order]["cost"])
    print(f"Your change is {win}$")
    money = money + float(MENU[order]["cost"])




def order_check(ingredients, price, order):
    global resources
    global MENU
    for item in resources:
        if float(drink['cost']) < float(price):
            money_work(price, order)

            if ingredients[item] > resources[item]:
                print("Not enough resources, call support")
                return False
            else:
                return True
        else:
            print("You need to insert more money")
            return False



order_success = True
is_on = True

while is_on:
    coins = input("Enter your coins!")
    order = input("What would you like? (espresso/latte/cappuccino)")
    if order == "report":
        print(f"Money count is {money}")
        print(f"Water count is {resources['water']}")
        print(f"Milk count is {resources['milk']}")
        print(f"Coffee count is {resources['coffee']}")
    elif order == "off":
        is_on = False
        print("Machine is turnning off")
    else:
       drink = MENU[order]
       ingredients = drink["ingredients"]
       price = coins

       if order_check(ingredients, price, order):
           make_coffe(ingredients, order)
























