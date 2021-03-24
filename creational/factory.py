class SimplePizzaFactory:

    @staticmethod
    def create_pizza(kind):
        if kind == "cheese":
            return CheezePizza()
        elif kind == "pepperoni":
            return PepperoniPizza()

class Pizza:
    def prepare(self):
        raise NotImplementedError

    def bake(self):
        raise NotImplementedError

    def cut(self):
        raise NotImplementedError

    def box(self):
        raise NotImplementedError

class CheezePizza(Pizza):
    def prepare(self):
        pass

    def bake(self):
        pass

    def cut(self):
        pass

    def box(self):
        pass


class PepperoniPizza(Pizza):

    def prepare(self):
        pass

    def bake(self):
        pass

    def cut(self):
        pass

    def box(self):
        pass


class PizzaStore:

    def order_pizza(self, kind):
        pizza = SimplePizzaFactory.create_pizza(kind)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

