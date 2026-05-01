def exercise5(nested: list | object) -> list | object:
    if type(nested) is not list:
        return [nested]
    result = []
    for l in nested:
        result += exercise5(l)
    return result

if __name__ == "__main__":
   print(exercise5([1,[2,3],[4,[5,6]],7]))
