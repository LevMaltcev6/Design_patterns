
class ChocolateBoiler:
    _instance = None

    def __init__(self):
        pass

    @staticmethod
    def get_instance():
        if not ChocolateBoiler._instance:
            ChocolateBoiler._instance = ChocolateBoiler.__ChocolateBoiler()
        return ChocolateBoiler._instance

    class __ChocolateBoiler:

        def __init__(self):
            self.empty = True
            self.boiled = False

        def fill(self):
            if self.empty:
                self.empty = False
                self.boiled = False

        def drain(self):
            if not self.empty and self.boiled:
                self.empty = True

        def boil(self):
            if not self.empty and not self.boiled:
                self.boiled = True


if __name__ == "__main__":
    s1 = ChocolateBoiler()
    s2 = ChocolateBoiler()

    print(dir(s1.get_instance()))


    print(s1.get_instance()==s2.get_instance())

