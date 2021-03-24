class CaffeineBeverage:

    def __init__(self):
        pass

    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def brew(self):
        raise NotImplementedError

    def add_condiments(self):
        raise NotImplementedError

    def boil_water(self):
        print("I boild water")

    def pour_in_cup(self):
        print("I pour in cup")

class Coffee(CaffeineBeverage):

    def brew(self):
        print("brew coffeinum")

    def add_condiments(self):
        print("add coffeinum")

class Tea(CaffeineBeverage):

    def brew(self):
        print("brew tea trees")

    def add_condiments(self):
        print("add tea")

# ---------------------------------------
class CaffeineBeverageWithHook:

    def __init__(self):
        pass

    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.wants_condiments():
            self.add_condiments()

    def brew(self):
        raise NotImplementedError

    def add_condiments(self):
        raise NotImplementedError

    def boil_water(self):
        print("I boild water")

    def pour_in_cup(self):
        print("I pour in cup")

    def wants_condiments(self):
        return True



class CoffeeWithHook(CaffeineBeverageWithHook):
    def brew(self):
        print("brew coffeinum")

    def add_condiments(self):
        print("add coffeinum")

    def wants_condiments(self):
        prompt = "Would you like milk and sugar with your coffee (y/n)?"
        answer = input(prompt)
        return answer.lower().startswith('y')



class TeaWithHook(CaffeineBeverageWithHook):
    def brew(self):
        print("brew coffeinum")

    def add_condiments(self):
        print("add coffeinum")

    def wants_condiments(self):
        prompt = "Would you like lemmon with your tea (y/n)?"
        answer = input(prompt)
        return answer.lower().startswith('y')




if __name__ == '__main__':
    tea = Tea()
    coffee = Coffee()

    print("\nMaking tea...")
    tea.prepare_recipe()

    print("\nMaking coffee...")
    coffee.prepare_recipe()

    tea_with_hook = TeaWithHook()
    coffee_with_hook = CoffeeWithHook()

    print("\nMaking tea...")
    tea_with_hook.prepare_recipe()

    print("\nMaking coffee...")
    coffee_with_hook.prepare_recipe()




