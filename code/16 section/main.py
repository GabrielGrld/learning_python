#import another_module
#print(another_module.another_variable)



# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("blue", "green")
# timmy.forward(100)
# timmy.forward(100)
# timmy.right(25)
#
# my_screen = Screen()
# print(my_screen.canvheight)
#
# my_screen.exitonclick()


# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# print(table)
# table.align ="l"
# print(table)


from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
profit = 0
while is_on:
    menu = Menu()
    choice = input(f"​What would you like? ({menu.get_items()}): ")
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    if choice == "report":
        coffee_maker.report()
        money_machine.report()

    elif choice == "off":
        is_on = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            money_machine.make_payment(drink.cost)
            coffee_maker.make_coffee(drink)
            print("se hace la bebida")
        else:
            print("no es suficiente")



