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

OFF=0
while OFF==0:
    profit=0


    choice=input("What would you like? Choose from: espresso/latte/cappuccino: \nor 'OFF' to turn off the machine: ")
    if choice=="latte" and resources['water']<200 or resources['coffee']<24 or resources['milk']<150:
     print("Sorry,Not enough resources for latte")
    elif choice=='OFF':
        exit()
    elif choice=="latte" and resources['water']>=200 and resources['coffee']>=24 and resources['milk']>=150:

         #the money that customer it's entering inside the coffee machine
        coffee_price=(MENU['latte']['cost'])
        print(f"The price for 1 cup of latte is: {coffee_price} dollars \nPlease insert coins:")
        quarters=int(input("How many quarters: "))
        dimes = int(input("How many dimes: "))
        nickles =int(input("How many nickles: "))
        pennies = int(input("How many pennies: "))
        user_coins=(quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)
        if user_coins>=coffee_price:
            print(f"Here is your {coffee_price-user_coins:.2f} $ change\nHere is your latte ☕. Enjoy")
            profit+=2.5
            resources['water'] -= 200
            resources['coffee'] -= 24
            resources['milk'] -= 150
        else:
            print("That's not enough money for the espresso. Money refunded")
    elif choice=="espresso" and resources['water']<50 or resources['coffee']<18 :
        print("Sorry,Not enough resources for espresso")
    elif choice=="espresso" and resources['water']>=50 and resources['coffee']>=18:

         #the money that customer it's entering inside the coffee machine
        coffee_price=(MENU['espresso']['cost'])
        print(f"The price for 1 cup of espresso is: {coffee_price} $ \nPlease insert coins.")
        quarters=int(input("How many quarters: "))
        dimes = int(input("How many dimes: "))
        nickles =int(input("How many nickles: "))
        pennies = int(input("How many pennies: "))
        user_coins=(quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)
        if user_coins>=coffee_price:
            print(f"Here is your {coffee_price-user_coins:.2f} $ change\nHere is your espresso ☕️. Enjoy")
            profit+=1.5
            resources['water'] -= 50
            resources['coffee'] -= 18
        else:
            print("That's not enough money for the espresso. Money refunded")

    elif choice=="cappuccino" and resources['water']<300 or resources['coffee']<100 or resources['milk']<200:
        print("Sorry,Not enough resources for cappuccino")
    elif choice=="cappuccino" and resources['water']>=300 and resources['coffee']>=100 and resources['milk']>=200:

        #the money that customer it's entering inside the coffee machine
        coffee_price=(MENU['cappuccino']['cost'])
        print(f"The price for 1 cup of cappuccino is: {coffee_price} $ \nPlease insert coins.")
        quarters=int(input("How many quarters: "))
        dimes = int(input("How many dimes: "))
        nickles =int(input("How many nickles: "))
        pennies = int(input("How many pennies: "))
        user_coins=(quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)
        if user_coins>=coffee_price:
            print(f"Here is your {coffee_price-user_coins:.2f} $ change\nHere is your cappuccino ☕️. Enjoy")
            profit+=3.0
            resources['water'] -= 300
            resources['coffee'] -= 100
            resources['milk'] -= 200
        else:
            print("That's not enough money for the cappuccino. Money refunded")

    else:
        print("That's not a coffee! Please select one from the offer!")






