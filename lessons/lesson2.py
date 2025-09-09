class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self,):
        print(f"{self.name} Base action")


#Дочерний класс
class HeroMage(Hero):
    def cast_spell(self):
        print(f"{self.name} fire!!")

class HeroWar(HeroMage):
    pass


kiritp = HeroMage("kirito", 100, 1000)
asuna = HeroWar("Asuna", 100, 1000)


class BaseUser:
    
