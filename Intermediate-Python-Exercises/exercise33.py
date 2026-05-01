from functools import lru_cache
from time_function import timer

@lru_cache(maxsize=1000)
def exercise33(N: int) -> int:
    if N < 2:
        return N
    return exercise33(N-2) + exercise33(N-1)

def test(N: int) -> int:
    if N < 2:
        return N
    return exercise33(N-2) + exercise33(N-1)
if __name__ == "__main__":
    faster = timer(lambda n: exercise33(n))
    slower = timer(lambda n: test(n))
    print(faster(1992))
    print(slower(1992))
    print(faster(1991))
    print(slower(1991))
