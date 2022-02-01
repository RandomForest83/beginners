class Food: 

    def __init__(self) -> None:
        # self.pizza_dict = pizza_dict
        pass

    
    def pizza_dictionary(self):
        
        pizza_dict = {
        "pizza_1" : ["Margherita", 5], 
        "pizza_2" : ["Salami", 6], 
        "pizza_3" : ["Thunfish", 7]
        }
        return pizza_dict  

    def print_food(self, pizza_dict):
        for i in self.pizza_dict:
            print(f"Pizza: {self.pizza_dict[i]}")

if __name__ == "__main__":
    menu = Food()
    print(menu.pizza_dictionary())
   

#TODO: Add Nudeln Dictionary with a class method
# If I have more time, I can extend and I add ingredients in the food class.