from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from os import system
from art import logo

machine = CoffeeMaker()
mymenu = Menu()
#item = MenuItem()
cashflow = MoneyMachine()
off = False

print(logo)

while not off:
    choix = input(f"Que voulez-vous choisir? ({mymenu.get_items()}) : ").lower()
    if choix == "rapport":
        machine.report()
        cashflow.report()
    elif choix == "off":
        off = True
    elif choix == "fill":
        machine.fill_machine()
    elif mymenu.find_drink(choix) is not None:
        cafe = mymenu.find_drink(choix)
        if machine.is_resource_sufficient(cafe):
            if cashflow.make_payment(cafe.cost):
                machine.make_coffee(cafe)
    system('cls')
    print(logo)