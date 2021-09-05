class Bird:
    def __init__(self, name):
        self._name = name

    def make_sound(self):
        pass


class Crow(Bird):
    def __init__(self):
        Bird.__init__(self, 'Crow')

    def make_sound(self):
        print(f"crow says kk")


class Duck(Bird):
    def __init__(self):
        Bird.__init__(self, 'Duck')

    def make_sound(self):
        print("duck says quack quack")


# b1 = Bird('bird')
# b1.make_sound()

c1 = Crow()
c1.make_sound()

d1 = Duck()
d1.make_sound()
