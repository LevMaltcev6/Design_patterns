from abc import ABC, abstractmethod




class Quackable(ABC):

    @abstractmethod
    def quack(self):
        pass



class MallardDuck(Quackable):

    def quack(self):
        print("quack")

class RedHeadDuck(Quackable):

    def quack(self):
        print("quaaak")


class DuckCall(Quackable):

    def quack(self):
        print("quack")


class RubberDuck(Quackable):

    def quack(self):
        print("squeak")


class DuckSimulator:


    def simulate(self):
        mDuck = DuckFactory().createMallDuck()
        rhDuck = DuckFactory().createRedHDuck()
        fakeDuck = DuckFactory().createDuckCall()
        goose = DuckFactory().createGoose()
        rDUck = DuckFactory().createRubberDuck()

        nonDuck = QuackCounter(MallardDuck())


        Flock().add(mDuck)
        Flock().add(rhDuck)
        Flock().add(fakeDuck)
        Flock().add(goose)
        Flock().add(rDUck)
        Flock().quack()

        nonDuck.get_quacks()


    def duck(self, duck:Quackable):
        duck.quack()


class GooseType(ABC):

    @abstractmethod
    def hello(self):
        pass

class Goose(GooseType):

    def hello(self):
        print("Honk")


class GooseAdapter(Quackable):

    def __init__(self, goose:Goose):
        self.goose = goose

    def quack(self):
        self.goose.hello()


class QuackCounter(Quackable):
    num_of_quacks = 0

    def __init__(self, duck):
        self.duck = duck

    def quack(self):
        self.duck.quack()
        QuackCounter.num_of_quacks += 1

    def get_quacks(self):
        print(QuackCounter.num_of_quacks)



class DuckFactory:

    """
    This is Factory
    """

    def createMallDuck(self):
        return QuackCounter(MallardDuck())
    def createRedHDuck(self):
        return QuackCounter(RedHeadDuck())
    def createDuckCall(self):
        return QuackCounter(DuckCall())
    def createRubberDuck(self):
        return QuackCounter(RubberDuck())
    def createGoose(self):
        return GooseAdapter(Goose())


class Flock(Quackable):
    """
    This is iterator:) + Combiner
    """
    _quackers = []

    def add(self, duck:Quackable):
        Flock._quackers.append(duck)


    def quack(self):
        for qucker in Flock._quackers:
            qucker.quack()






sm = DuckSimulator()
sm.simulate()



