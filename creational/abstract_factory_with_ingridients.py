class Pizza:
    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.veggies = []
        self.cheese = None
        self.pepperoni = None
        self.clam = None

    def prepare(self):
        raise NotImplementedError

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")

    def get_name(self):
        return self.name


# realizations
class CheesePizza(Pizza):
    def __init__(self, ingredient_factory):
        super().__init__()
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print("Preparing " + self.name)
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()


class ClamPizza(Pizza):
    def __init__(self, ingredient_factory):
        super().__init__()
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print("Preparing " + self.name)
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.clam = self.ingredient_factory.create_clam()


class PizzaStore:
    def create_pizza(self, kind):
        raise NotImplementedError

    def order_pizza(self, kind):
        pizza = self.create_pizza(kind)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class NYStylePizzaStore(PizzaStore):
    def create_pizza(self, kind):
        pizza = None
        ingredient_factory = NYPizzaIngredientFactory()
        if "cheese" == kind:
            pizza = CheesePizza(ingredient_factory)
            pizza.name = "New York Style Cheese Pizza"
        elif "pepperoni" == kind:
            pizza = ClamPizza(ingredient_factory)
            pizza.name = "New York Style Pepperoni Pizza"
        elif "clam" == kind:
            pizza = ClamPizza(ingredient_factory)
            pizza.name = "New York Style Clam Pizza"
        elif "veggie" == kind:
            pizza = ClamPizza(ingredient_factory)
            pizza.name = "New York Style Veggie Pizza"
        return pizza


"""Pizza Ingridient Factory Interface"""
class PizzaIngredientFactory:
    def create_dough(self):
        raise NotImplementedError

    def create_sauce(self):
        raise NotImplementedError

    def create_cheese(self):
        raise NotImplementedError

    def create_veggies(self):
        raise NotImplementedError

    def create_pepperoni(self):
        raise NotImplementedError

    def create_clam(self):
        raise NotImplementedError



class ThinCrustDough:
    pass


class MarinaraSauce:
    pass


class ReggianoCheese:
    pass


class Veggies:
    pass


class Garlic(Veggies):
    pass


class Onion(Veggies):
    pass

class Mushroom(Veggies):
    pass


class RedPepper(Veggies):
    pass


class SlicedPepperoni:
    pass


class FreshClams:
    pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):

    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        return MarinaraSauce()

    def create_cheese(self):
        return ReggianoCheese()

    def create_veggies(self):
        return [Garlic(), Onion(), Mushroom(), RedPepper()]

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FreshClams()


class ThickCrustDough:
    pass


class PlumTomatoSauce:
    pass


class Mozzarella:
    pass


class EggPlant(Veggies):
    pass


class Spinach(Veggies):
    pass


class BlackOlives(Veggies):
    pass


class FrozenClams:
    pass


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):

    def create_dough(self):
        return ThickCrustDough()

    def create_sauce(self):
        return PlumTomatoSauce()

    def create_cheese(self):
        return Mozzarella()

    def create_veggies(self):
        return [EggPlant(), Spinach(), BlackOlives()]

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FrozenClams()


nyPizzaStore = NYStylePizzaStore()
# chicagoPizzaStore = ChicagoStylePizzaStore()
pizza = nyPizzaStore.order_pizza("cheese")
print(f"Ethan ordered a {pizza.get_name()}\n")
# pizza = chicagoPizzaStore.order_pizza("cheese")
# print(f"Joel ordered a {pizza.get_name()}\n")

