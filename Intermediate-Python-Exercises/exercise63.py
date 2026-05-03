def exercise63(message: str, shift: int) -> str:
    return "".join(chr((ord(c)-65+shift)%26+65) if c.isupper() else chr((ord(c)-97+shift)%26+97) if c.islower() else c for c in message)
if __name__ == "__main__":
    import string
    # 65-90 97-122
    # print(*(ord(c) for c in string.ascii_letters),sep="\n")
    print(exercise63("Hello!",3))
