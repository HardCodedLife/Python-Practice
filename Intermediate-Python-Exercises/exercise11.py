def exercise11(d1: dict[str,int], d2: dict[str, int]) -> dict[str,list[int]]:
    return {k: ([d1[k]] if k in d1 else []) +([d2[k]] if k in d2 else [])  for k in set(d1) | set(d2)}
if __name__ == "__main__":
    print(exercise11({"a": 1, "b": 2},{"b": 3, "c": 4}))
