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


is_on=True
price=0


def isResourceSufficient(ingridient):
    for item in ingridient:
        if ingridient[item]>= resources[item]:
            print(f"“Sorry there is not enough {item}.")
            return False
    return True

def processCoin():
    print("Please inser coins")
    total=int(input("How many quaters?: "))*0.25
    total+=int(input("How many quaters?: "))*0.1
    total+=int(input("How many quaters?: "))*0.05
    total+=int(input("How many quaters?: "))*0.01
    return total

def changeResources(ingredients,cost):
    for item in ingredients:
        resources[item]-=ingredients[item]
    global price
    price+=cost


while is_on:
    choice=input("What would you like? (espresso/latte/cappuccino): ")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money: ${price}")

    elif choice=="espresso"or choice=="latte" or choice=="cappuccino":
        drink=MENU[choice]
        if isResourceSufficient(drink["ingredients"]):
            total_money=processCoin()
            if total_money>=drink["cost"]:
                changeResources(drink["ingredients"],drink["cost"])
                change=round(total_money-drink["cost"],2)
                print(f"Here is ${change} in change.")
                print(f"Here is your {choice} ☕, Enjoy! ")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            continue
    else:
        print("Invalid input! try again")
