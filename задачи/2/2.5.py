class Nikola:
    def __init__(self, name, age):
        self.name = name if name == "Николай" else f"Я не {name}, а Николай"
        self.age = age


person1 = Nikola("Максим", 30)
print(person1.name)  

person2 = Nikola("Николай", 25)
print(person2.name) 
