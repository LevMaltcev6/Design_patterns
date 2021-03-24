class Beverage:

    def __init__(self):
        self.description = "Unknown beverage"

    def get_description(self):
        pass

    def cost(self):
        pass

    # 0,1,2
    def set_size(self, size):
        pass

    def get_size(self):
        pass


class CondimentDecorator(Beverage):

    def get_description(self):
        raise NotImplementedError

    def cost(self):
        raise NotImplementedError

    def get_size(self):
        pass


# --------------product
class Espresso(Beverage):

    def __init__(self, size=0):
        super().__init__()
        self.description = "Espresso"
        self.size = size

    def cost(self):
        return 1.99

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size


# ----------------- upsale
class Mocha(CondimentDecorator):

    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Mocha"

    # def cost(self):
    #     return 0.20 + self.beverage.cost()
    def get_size(self):
        return self.beverage.get_size()

    def cost(self):
        return 0.1+(0.5*(self.get_size())) + self.beverage.cost()


class Soy(CondimentDecorator):

    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage

    def get_description(self):
        return self.beverage.description + ", Soy"

    def get_size(self):
        return self.beverage.get_size()

    def cost(self):
        return 0.1 + self.beverage.cost()


class SteamedMilk(CondimentDecorator):
    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Steamed Milk"

    def get_size(self):
        return self.beverage.get_size()

    def cost(self):
        return 0.10 + self.beverage.cost()



if __name__ == "__main__":
    b = Espresso()
    print(b.cost())
    b = Mocha(b)
    print(b.cost())
    b = Mocha(b)
    b = SteamedMilk(b)
    print(b.cost())


