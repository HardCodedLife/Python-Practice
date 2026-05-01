def exercise27(nums: list[int]) -> list[int]:
    return map(lambda x: x**2, filter(lambda x: True if x%2 == 0 else False, nums))
if __name__ == "__main__":
    print(*exercise27([1, 2, 3, 4, 5, 6]))
