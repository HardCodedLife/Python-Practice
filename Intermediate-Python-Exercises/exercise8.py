def exercise8(strings: list[str]) -> list[str]:
    return [s for s in strings if len(s)>5 and s[0] in ['a','e','i','o','u']]

if __name__ == "__main__":
    print(exercise8(["apple", "education", "ice", "ocean", "python", "umbrella"]))
