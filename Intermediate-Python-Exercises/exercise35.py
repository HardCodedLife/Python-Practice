class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def fuel_type():
        pass
class ElectircCar(Vehicle):
    def fuel_type(self):
        return "Electircity"
if __name__ == "__main__":
    car = ElectircCar("Tesla")
    print(car.brand)
    print(car.fuel_type())
