class Soda:
    def __init__(self, add_on=None):
        self.add_on = add_on
    
    def show_my_drink(self):
        if self.add_on:
            print(f"Газировка и {self.add_on}")
        else:
            print("Обычная газировка")


soda1 = Soda("лимон")
soda1.show_my_drink()  

soda2 = Soda()
soda2.show_my_drink()  
