def flatten(nested: list) -> list:
    if not nested:
        return []
    head, *tail = nested

    if type(head) == list:
        head = flatten(head)
    else:
        head = [head]

    return head + flatten(tail)

if __name__ == "__main__":
   print(flatten([1,[2,3],[4,[5,6]],7]))
