class Pizza:
    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.toppings = None

    def prepare(self):
        print(f"Preparing {self.name}")
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings: ")
        for topping in self.toppings:
            print(f"  {topping}")

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")

    def get_name(self):
        return self.name


class NYStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NY Style Sauce and Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings = ["Grated Reggiano Cheese"]

    

class NYStylePepperoniPizza(Pizza):
    pass


class NYStyleClamPizza(Pizza):
    pass


class NYStyleVeggiePizza(Pizza):
    pass

class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Deep Dish Cheese Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings = ["Shredded Mozzarella Cheese"]

    def cut(self):
        print("Cutting the pizza into square slices")

class ChicagoStylePepperoniPizza(Pizza):
    pass


class ChicagoStyleClamPizza(Pizza):
    pass

class CaliforniaStyleCheesePizza(Pizza):
    pass


class CaliforniaStylePepperoniPizza(Pizza):
    pass

"""Interface"""
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
        chooser = {
            "cheese": NYStyleCheesePizza(),
            "pepperoni": NYStylePepperoniPizza(),
            "clam": NYStyleClamPizza(),
            "veggie": NYStyleVeggiePizza()
        }
        return chooser.get(kind)


class ChicagoStylePizzaStore(PizzaStore):
    def create_pizza(self, kind):
        chooser = {
            "cheese": ChicagoStyleCheesePizza(),
            "pepperoni": ChicagoStylePepperoniPizza(),
            "clam": ChicagoStyleClamPizza(),
        }
        return chooser.get(kind)


class CaliforniaStylePizzaStore(PizzaStore):
    def create_pizza(self, kind):
        chooser = {
            "cheese": CaliforniaStyleCheesePizza(),
            "pepperoni": CaliforniaStylePepperoniPizza()
        }
        return chooser.get(kind)


nyPizzaStore = NYStylePizzaStore()
chicagoPizzaStore = ChicagoStylePizzaStore()
pizza = nyPizzaStore.order_pizza("cheese")
print(pizza)
# print(f"Ethan ordered a {pizza.get_name()}\n")
# pizza = chicagoPizzaStore.order_pizza("cheese")
# print(f"Joel ordered a {pizza.get_name()}\n")



