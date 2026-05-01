class CPU:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"{self.name} CPU"
class RAM:
    def __init__(self, capacity):
        self.capacity = capacity
    def __str__(self):
        return f"{self.capacity} RAM"
class Computer:
    def __init__(self, name, capacity):
        self.cpu = CPU(name)
        self.ram = RAM(capacity)
    def __str__(self):
        return f"Computer with {self.cpu} and {self.ram}"
if __name__ == "__main__":
    print(Computer("Intel i7", "16GB"))
