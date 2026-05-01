from collections.abc import Generator


def exercise32(names: list[str], scores: list[int]) -> Generator:
    return (f"Rank {i+1}: {line[0]} scored {line[1]}" for i, line in enumerate(sorted(zip(names,scores), reverse= True,key=lambda x: x[1])))
if __name__ == "__main__":
    print(*exercise32(["Alice", "Bob", "Charlie"],[85, 92, 78]), sep='\n')
