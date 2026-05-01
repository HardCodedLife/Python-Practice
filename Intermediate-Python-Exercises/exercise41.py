class Flyer:
    def fly(self):
        print("Flying high!")

class Swimmer:
    def swim(self):
        print("Swimming fast!")

class Duck(Swimmer, Flyer): pass
if __name__ == "__main__":
    d = Duck()
    d.fly()
    d.swim()
    print(Duck.mro())
