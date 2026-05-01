def exercise9(duplicates: list) -> list:
    seen = []
    return [seen.append(e) or e for e in duplicates if e not in seen]


if __name__ == "__main__":
    print(exercise9([1, 2, 2, 3, 1, 4, 2]))

