def exercise54(text: str) -> int:
    return sum((
    any(c.isupper() for c in text),
    any(c.islower() for c in text),
    any(c.isdigit() for c in text),
    True if len(text)>=8 else False,
    any(not c.isalnum() and not c.isspace() for c in text),
    ))
if __name__ == "__main__":
    print(exercise54("P@ssword123"))
