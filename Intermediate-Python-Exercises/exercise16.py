from itertools import combinations

def exercise16(A: list[int]) -> list[set[int]]:
    return [s for i in range(len(A)) for s in combinations(A, i+1)]
if __name__ == "__main__":
    print(exercise16([1,2,3]))
