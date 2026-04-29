def exercise10(lst: list, n: int, direction: str) -> list:
    n = n % l if n > (l:=len(lst)) else n
    if direction == 'right':
        lst = lst[-n:] + lst[:-n] 
    elif direction == 'left':
        lst = lst[n+1:] + lst[:n+1]
    return lst
if __name__ == "__main__":
    print(exercise10([1, 2, 3, 4, 5], 2, 'right'))
