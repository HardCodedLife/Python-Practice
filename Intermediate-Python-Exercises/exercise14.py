def exercise14(A: list[int], B: list[int]) -> str:
    A, B = set(A), set(B)
    return "Superset" if A>B else "Subset" if B>A else "Disjoint" if A&B == set() else "Unknown"

if __name__ == "__main__":
    print(exercise14({1, 2, 3},{1, 2, 3, 4, 5}))
