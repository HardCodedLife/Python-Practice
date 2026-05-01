class Student:
    def __init__(self, name) -> None:
        self.name = name
        self.score = 0
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name: str):
        if type(name) is not str:
            raise TypeError('Name must be a "str"')
        self._name = name
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score: int):
        if score>100 or score<0:
            raise ValueError('Score must be between 0 and 100.')
        self._score = score
if __name__ == "__main__":
    s = Student("Kevin")
    s.score = 105
