def exercise15(list1: list[int], list2: list[int]) -> set[int]:
    A, B = set(list1), set(list2)
    return A^B
if __name__ == "__main__":
    print(exercise15([101, 102, 103],[103, 104, 105]))
