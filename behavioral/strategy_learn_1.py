from abc import ABC, abstractmethod

class Weapon(ABC):

    @abstractmethod
    def use_weapon(self):
        pass


class Axe(Weapon):

    def use_weapon(self):
        print("use AXE")


class Gun(Weapon):

    def use_weapon(self):
        print("use Gun")

# ------------
class Character:

    def __init__(self):
        self.weapon = None

    def change_weapon(self, new_weapon:Weapon):
        self.weapon = new_weapon

    def fight(self):
        self.weapon.use_weapon()

class King(Character):

    def __init__(self):
        super().__init__()
        self.weapon = Gun()

class Chort(Character):

    def __init__(self):
        super().__init__()
        self.weapon = Axe()


if __name__ == "__main__":
    king = King()
    king.fight()
    king.change_weapon(Axe())
    king.fight()




