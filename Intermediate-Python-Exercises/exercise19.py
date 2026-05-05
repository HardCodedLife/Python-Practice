from datetime import date, timedelta
def exercise19(start_date: str, N: int) -> str:
    start_date = date.fromisoformat(start_date)
    s = start_date.weekday() + 1
    delta = 0
    weekdays = 0
    while weekdays != N:
        s %= 7
        if s != 5 and s != 6:
            weekdays += 1
        delta += 1
        s += 1
    return (start_date + timedelta(days=delta)).strftime("%A, %Y-%m-%d")
if __name__ == "__main__":
    print(exercise19('2026-01-02', 5))
