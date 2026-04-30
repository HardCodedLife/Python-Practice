def exercise25(sorted_list: list, target: object) -> int:
    if (l:=len(sorted_list)) <= 1 and sorted_list[0] != target:
        return None
    index = l // 2
    if sorted_list[index] == target:
        return index
    elif sorted_list[index] > target:
        index = exercise25(sorted_list[:index], target)
    elif sorted_list[index] < target:
        index = index + r if (r := exercise25(sorted_list[index:], target)) is not None else None
    return index
if __name__ == "__main__":
    print(exercise25([10, 20, 30, 40, 50, 60],50))
