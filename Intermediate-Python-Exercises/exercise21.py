def exercise21(numbers: list[int]) -> set[int]:
    seen = set()
    return {i for i in numbers if i in seen or seen.add(i) }
if __name__ == "__main__":
    print(exercise21([1, 2, 3, 2, 4, 5, 1, 6]))
