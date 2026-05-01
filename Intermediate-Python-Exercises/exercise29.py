from collections.abc import Generator


def exercise29(N: int) -> Generator:
    f, s = 0, 1
    yield f
    yield s
    yield from ("wrong" if (f:=s)<0 else (s:=current) for i in range(2,N) if (current:=f+s))
if __name__ == "__main__":
    print(*exercise29(8))
