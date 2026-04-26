def exercise1(words: list[str]) -> tuple[str, ...]:
    return (word.upper() for word in words if len(word)>=4)
if __name__=="__main__":
    print(*exercise1(["apple", "bat", "cherry", "dog", "elderberry"]))
