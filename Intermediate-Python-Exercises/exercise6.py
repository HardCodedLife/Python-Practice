def exercise6(sentence: str) -> str:
    return ' '.join([word[::-1] for word in sentence.split()])

if __name__ == "__main__":
    print(exercise6("Python is awsome"))
