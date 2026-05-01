def exercise34(trial: list[int], paid: list[int]) -> None:
    trial = set(trial)
    paid = set(paid)
    print(f"Both: {trial & paid}")
    print(f"Trial only: {trial - paid}")
    print(f"Not both: {trial ^ paid}")
if __name__ == "__main__":
    exercise34([1, 2, 3, 4, 5],[4, 5, 6, 7, 8])
