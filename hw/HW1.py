
class Animal:
    def __init__(self, name, age, sound ):
        self.name = name
        self.age = age
        self.sound = sound
    def action(self):
        return f"{self.name} издает звук: {self.sound}"

animal1 = Animal("Кот", 3, "мяу" )
animal2 = Animal("Собавка", 1, "гав")

print(animal1.action())
print(animal2.action())

    


