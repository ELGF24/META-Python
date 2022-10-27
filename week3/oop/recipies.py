

class Recipe():
    
    def __init__(self, dish, items, time):
        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        return f"The {self.dish} has {self.items} and takes {self.time} min to prepare"


pizza = Recipe("pizza", ["cheese", "bread", "tomato"], 45)
pasta = Recipe("pasta", ["cheese", "tomato"], 35)

print(pizza.contents())
print(pasta.contents())
print(pizza.items)