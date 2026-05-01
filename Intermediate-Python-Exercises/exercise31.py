def exercise31(event: str, *args, **kwargs) -> None:
    print(f"Event: {event}")
    print(f'Details: {args}')
    print(f'Metadata: {kwargs}')
if __name__ == "__main__":
    exercise31("User Login", "admin", "dashboard", timestamp="10:00 AM", status="Success")
