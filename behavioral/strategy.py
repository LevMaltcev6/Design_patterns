from abc import ABC, abstractmethod
# Вообще правильнее бы сделать Fly_behavior как ABC класс, а fly в нем как abstractclass, тогда будет более явная функциональность

"""================
Fly behaviors
"""
class Fly_behavior:

    def fly(self):
        raise NotImplementedError

class Fly_with_wings(Fly_behavior):
    def fly(self):
        print("fly with wings")

class Fly_Not(Fly_behavior):
    def fly(self):
        print("Cant fly")

# -----------------------
"""======================
Quack behaviors
"""
class Quack_behavior:

    def quack(self):
        raise NotImplementedError

class Quack(Quack_behavior):

    def quack(self):
        print("QUACK")

class Squeak(Quack_behavior):
    def quack(self):
        print("SQUEAK")

class MuteQuak(Quack_behavior):
    def quack(self):
        print("cant quack")

"""================
Duck classes
"""
class Duck:
    def __init__(self):
        self.fly_type = None
        self.quack_type = None

    def set_fly(self, fly_type):
        self.fly_type = fly_type

    def set_quack(self, quack_type):
        self.quack_type = quack_type

    def perform_fly(self):
        self.fly_type.fly()

    def perform_quack(self):
        self.quack_type.quack()


class MallardDuck(Duck):

    def __init__(self):
        super().__init__()
        self.fly_type = Fly_Not()
        self.quack_type = Squeak()




if __name__ == "__main__":
    mallard = MallardDuck()
    mallard.perform_quack()
    mallard.perform_fly()
    mallard.set_fly(Fly_with_wings())
    mallard.perform_fly()































