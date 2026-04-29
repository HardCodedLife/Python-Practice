from collections import Counter
def exercise3(text: str) -> dict[str:int]:
    text = text.replace(' ','').lower()
    return Counter(text)

if __name__ == "__main__":
    print(exercise3("Python Programming"))
