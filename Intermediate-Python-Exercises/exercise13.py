def exercise13(employees: list[dict]) -> list[dict]:
    return employees.sort(reverse= True, key = lambda x: x['salary']) or employees
if __name__ == "__main__":
    print(exercise13([{"name": "A", "salary": 50}, {"name": "B", "salary": 70}, {"name": "C", "salary": 60}]))
