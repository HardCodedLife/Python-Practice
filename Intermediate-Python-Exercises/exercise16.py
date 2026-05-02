from itertools import combinations

def exercise16(A: list[int]) -> list[set[int]]:
    return [s for i in range(len(A)+1) for s in combinations(A, i)]
if __name__ == "__main__":
    print(exercise16([1,2,3]))
