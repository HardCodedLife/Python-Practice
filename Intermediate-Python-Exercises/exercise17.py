from datetime import date
from dateutil.relativedelta import relativedelta
def exercise17(birthday: str, today: str = "") -> str: 
    return f"Age: {(age := relativedelta(date.fromisoformat(today) if today else date.now(), date.fromisoformat(birthday)) )
.years} years, {age.months} months, {age.days} days" 

if __name__ == "__main__":
    print(exercise17("1995-05-15","2026-01-02"))
