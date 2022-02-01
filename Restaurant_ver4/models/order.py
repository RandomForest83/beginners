# if user enters martherita, we need to access the class food and the values from the dictionary, save it to a variable and then sum the price 
from food import Food


class Order: 

    def __init__(self, pizza) -> None:
        self.pizza = pizza
        print("Just for fun", self.pizza)
        
    def user_input(self):

        pizza_list = []
        
        while True:
            input_outside = input("Enter the name of the pizza: ")
            if input_outside == '0':
                break
            if input_outside == "Margherita" or input_outside == "Salami" or input_outside == "Thunfish":
                pizza_list.append(input_outside)
            else: 
                print("We don't have this on the menu.")
        
            print(pizza_list)
                
        if input_outside == "Margherita":
            show_food = Food.pizza_dictionary(self)
            print(show_food)
        
        return pizza_list





# menu = Food.pizza_dictionary()
# input("Enter the name of the pizza: ")