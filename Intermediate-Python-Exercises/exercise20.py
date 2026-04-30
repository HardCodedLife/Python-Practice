class PowerOfTwo:
    def __init__(self, N) -> None:
        self.power = N
        self.current_power = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current_power > self.power:
            raise StopIteration
        result = 2**self.current_power
        self.current_power += 1
        return result
if __name__ == "__main__":
        print(*PowerOfTwo(3))
