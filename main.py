from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

decision = input("What would you like? " + Menu().get_items() + ":")

available_drinks = Menu().get_items().split("/")
print(CoffeeMaker().report())


def drinks(drink):
    resource_sufficiency = CoffeeMaker().is_resource_sufficient(Menu().find_drink(drink))
    if resource_sufficiency:
        paid = False
        while not paid:
            print("Please insert coins.  quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01")
            paid = MoneyMachine().make_payment(Menu().find_drink(drink).cost)
            if paid:
                o = Menu().find_drink(drink)
                CoffeeMaker().make_coffee(o)
                print(MoneyMachine().report())
                print(CoffeeMaker().report())

    else:
        print(resource_sufficiency)
        # later add return message what resource is insufficient (if any is)


if decision == "off":
    exit()
elif decision == "report":
    print(CoffeeMaker().report())
else:
    for drink in available_drinks:
        if decision == drink:
            drinks(drink)
