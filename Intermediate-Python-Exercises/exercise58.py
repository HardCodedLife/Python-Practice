import re
def exercise58(email: str) -> bool:
    return True if re.fullmatch(r"^[\w\d]+[^!*\\/@]*[\w\d]+@\w+(\.\w+)?\.\w{2,3}$", email) else False
if __name__ == "__main__":
    print(exercise58("python_pro@gmail.com"))
    print(exercise58('john doe"@example.com'))
    print(exercise58(".user@ex.com"))
    print(exercise58("user.@ex.com"))
    print(exercise58("bad-email@com"))
    print(exercise58("firstname.lastname@example.com"))
    print(exercise58("jane.doe123@domain.co"))
    print(exercise58("username@mail.example.com"))
    print(exercise58("user+tag@example.com"))
    print(exercise58("john.doe@gmail.com"))
    print(exercise58("jane_doe@company.org"))
    print(exercise58("info-desk@sub.domain.net"))
    print(exercise58("123456@numbers.com"))
    print(exercise58("first.last+newsletter@example.com"))
    print(exercise58(""))
