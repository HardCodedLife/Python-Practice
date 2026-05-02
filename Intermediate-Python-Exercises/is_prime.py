def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    else:
        return True
if __name__ == "__main__":
    print(is_prime(2))
    print(is_prime(97))
    print(is_prime(88))
    print(is_prime(89))
