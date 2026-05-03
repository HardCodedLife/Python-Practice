import secrets
import string
def exercise60(length: int) -> str:
    return "".join(secrets.choice(string.ascii_letters + string.digits + string.punctuation+ " ") for i in range(length))
if __name__ == "__main__":
    print(exercise60(12))
