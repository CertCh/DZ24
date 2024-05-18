class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def increase_quantity(self, amount):
        self.quantity += amount
    
    def decrease_quantity(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
        else:
            print("Недостаточно товара на складе")
    
    def total_cost(self):
        return self.price * self.quantity


product = Product("Apple", 10, 50)
product.increase_quantity(10)
product.decrease_quantity(5)
print(product.total_cost()) 
