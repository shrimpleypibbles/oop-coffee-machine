from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

while is_on:
    sirCoffee = CoffeeMaker()
    sirMoney = MoneyMachine()
    sirMenu = Menu()
    options = sirMenu.get_items()
    order_name = input(f"What drink would you like?: {options}")
    if order_name == "report":
        sirCoffee.report()
        sirMoney.report()
    elif order_name == "off":
        print("Thank you for using sirCoffee. Have a nice day. ")
        is_on = False
    else:
        drink = sirMenu.find_drink(order_name)
        if sirCoffee.is_resource_sufficient(drink):
            if sirMoney.make_payment(drink.cost):
                sirCoffee.make_coffee(drink)
            else:
                print("Insufficient Funds. ")
        else:
            print("Insufficient Resources. ")




