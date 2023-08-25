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
    "final_money": 0

}

money = 0
def compare_ingredients(water_needed, milk_needed, coffee_needed):
    if resources["water"] >= water_needed and resources["milk"] >= milk_needed and resources["coffee"] >= coffee_needed:
        resources["water"] -= water_needed
        resources["milk"] -= milk_needed
        resources["coffee"] -= coffee_needed
    else:
        print("Insufficient resources to make coffee")
def make_coffe(water_needed, milk_needed, coffee_needed, cost, user_choice, money):
    print("Anavaible coins  $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01")
    counting_coins = True
    while counting_coins:
        print(f"Your choice is {user_choice}, your current wallet {money}, and the prize for the coffe {cost}")
        insert_coin = float(input("Insert a coin: "))
        coin1 = 0.25
        dimes = 0.10
        nickles = 0.05
        pennies = 0.01
        if insert_coin == coin1 or insert_coin == dimes or insert_coin == pennies or insert_coin == nickles:
            money +=  insert_coin
            if money == cost:
                print(f"Making a {user_choice} for you :)")
                counting_coins = False
                resources["final_money"] += money

            elif money >= cost:
                rest_of_the_money = money - cost
                print(f"Returning money for you {rest_of_the_money}")
                resources["final_money"] -= rest_of_the_money
                counting_coins = False

        else:
            print("Try again with a correct coin")
        compare_ingredients(water_needed, milk_needed, coffee_needed)
        print("Here is your latte. Enjoy!")





def disable_machine():
    turn_on = False

def print_report():
    for key,value in resources.items():
        print(key.capitalize() + ":",value)
turn_on = True
while turn_on:
    def start_machine():
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if user_choice == "report":
            print_report()
        else:
            result = check_resources(user_choice)
            if result is not None:
                water_needed, milk_needed, coffee_needed, cost, user_choice = check_resources(user_choice)
                make_coffe(water_needed, milk_needed, coffee_needed, cost, user_choice, money)

    def check_resources(user_choice):
        if user_choice in MENU:
            coffee_data = MENU[user_choice]
            coffee_ingredients = coffee_data["ingredients"]

            water_needed = coffee_ingredients.get("water", 0)
            milk_needed = coffee_ingredients.get("milk", 0)
            coffee_needed = coffee_ingredients.get("coffee", 0)

            cost = MENU[user_choice]["cost"]
            if water_needed <= resources["water"] and milk_needed <= resources["milk"] and coffee_needed <= resources["coffee"]:
                return water_needed, milk_needed, coffee_needed, cost, user_choice
            else:
                if water_needed > resources["water"]:
                    print("Insufficient water")
                if milk_needed > resources["milk"]:
                    print("Insufficient milk")
                if coffee_needed > resources["coffee"]:
                    print("Insufficient coffee")
                return None
        return None



    start_machine()