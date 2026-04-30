from datetime import datetime
def exercise18(current_date: str = '') -> str:
    now = datetime.fromisoformat(current_date) if current_date else datetime.now()
    new_year = datetime(now.year+1,1,1)
    diff = new_year - now
    days = diff.days
    remaining_seconds = diff.seconds
    hours, remaining_seconds = divmod(remaining_seconds, 60*60)
    minutes, remaining_seconds = divmod(remaining_seconds, 60)
    #result = f"{diff.days} days, {diff.seconds//(60*60)} hours, {diff.seconds%(60*60)//60} minutes"
    return f"{days} days, {hours} hours, {minutes} minutes"#result
if __name__ == "__main__":
    #print(exercise18("2026-01-02"))
    print(exercise18())
