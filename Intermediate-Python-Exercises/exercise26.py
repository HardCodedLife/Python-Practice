def exercise26(employees: list[tuple[str, int, int]]) -> list[tuple[str, int, int]]:
    return employees.sort(reverse=True, key=lambda x: x[2]) or employees
if __name__ == "__main__":
    print(exercise26([("Alice", 30, 50000), ("Bob", 25, 75000), ("Charlie", 35, 60000)]))
