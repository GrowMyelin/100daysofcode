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

def main():
    on = True
    while on:
        order = input('What would you like? (espresso/latte/cappuccino): ')
        if order == 'off':
            break
        ingredients = MENU[order]["ingredients"]
        total = MENU[order]['cost']
        print("Money: $" + str(total))
        for keys,values in ingredients.items():
            if keys == 'coffee':
                print(f"{keys}: {values}g")
            else:
                print(f"{keys}: {values}ml")
            if resources[keys] < values:
                print(f"Not enough {keys}.")
        print(f"Please insert coins. Total is ${total}")
        q = input("How many quarters?: ")
        total -= (int(q)*.25)
        print(f"Total left is {total}.")
        d = input("How many dimes?: ")
        total -= (int(d)*.1)
        print(f"Total left is {total}.")
        n = input("How many nickels?: ")
        total -= (int(n)*.05)
        print(f"Total left is {total}.")
        p = input("How many pennies?: ")
        total -= (int(p)*.01)
        if total == 0:
            print(f"Purchase is successful. Here is your {order}!")
        elif total > 0:
            print("Not enough money. Money refunded")
        elif total < 0:
            print(f"Purchase is successful. Here is your {order}!")
            print(f"Too much money. Here's {-total} in change.")

if __name__ == "__main__":
    main()