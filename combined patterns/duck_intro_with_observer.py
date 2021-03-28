
from abc import ABC, abstractmethod

class DuckObservable(ABC):

    @abstractmethod
    def notify_observers(self):
        pass

    @abstractmethod
    def register_observer(self, observer):
        pass


# Класс упрощенка для Quackable
class Observable(DuckObservable):
    _observers = []

    def __init__(self, duck):
        self.duck = duck

    def register_observer(self, observer):
        Observable._observers.append(observer)

    def notify_observers(self):
        for obs in Observable._observers:
            obs.update(self.duck)


# Наблюдатель интерфейс
class Observer(ABC):

    def update(self, duck):
        pass

# Наблюдатель
class Quackologist(Observer):

    def update(self, duck):
        print("Quack logist: %s - just quacked" % duck)


# ????
class Quackable(Observable):

    def __init__(self):
        super().__init__(self)

    @abstractmethod
    def quack(self):
        pass

class MallardDuck(Quackable):

    # def __init__(self):
    #     super().__init__(self)
    #     self.observable = Observable(self)

    def quack(self):
        print("quack")
        self.notify_observers()


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

        quackologist = Quackologist()

        Flock().register_observer(quackologist)
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
    """Goose interface"""

    @abstractmethod
    def hello(self):
        pass

class Goose(GooseType):
    """Real goose"""

    def hello(self):
        print("Honk")


class GooseAdapter(Quackable):
    """Goose adapter"""

    def __init__(self, goose:Goose):
        self.goose = goose

    def quack(self):
        self.goose.hello()


class QuackCounter(Quackable):
    """Decoreator for counting of quacks"""
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


class Flock(Quackable, Observable):
    """
    This is iterator:) + Combiner
    """
    _quackers = []

    def __init__(self, duck):
        super().__init__(duck)
        Flock._quackers.append(duck)

    def add(self, duck:Quackable):
        Flock._quackers.append(duck)


    def quack(self):
        for qucker in Flock._quackers:
            qucker.quack()
            super().notify_observers()


    def register_observer(self, obs):
        super().register_observer(obs)

    def notify_observers(self):
        super().notify_observers()





sm = DuckSimulator()
sm.simulate()



