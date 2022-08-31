from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    on = True
    menu = Menu()
    while on:
        orderStr = input(f"What would you like? ({menu.get_items()}): ")
        if orderStr == 'off':
            break

        order = menu.find_drink(orderStr)
        cMaker = CoffeeMaker()
        mMachine = MoneyMachine()
        print(f"Cost is: ${order.cost}")
        print(order.ingredients)
        if cMaker.is_resource_sufficient(order):
            cMaker.make_coffee(order)
        else:
            print("Not enough resources")

if __name__ == "__main__":
    main()