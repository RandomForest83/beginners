from food import Food
# from models.drink import Drink
from order import Order
from bill import Bill 

class Menu: 

    def show_pizza(self):
        Food.pizza_dictionary(self)

"""    
    def show_drinks(self):
        for i in self.drink_list:
            print(f'Drinks: {i}')
"""

# Show Restaurant Menu
# menu_1.show_menu_food()
# menu_1.show_menu_drinks()

user = Order('Margherita')
pizza_list = user.user_input()
# menu_1 = Menu()
# menu_1.show_pizza()

user_bill = Bill() 
user_bill.billing(pizza_list)

