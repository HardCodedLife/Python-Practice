from is_prime import is_prime
def exercise57(start_from: int, end_at: int) :
    return (i for i in range(start_from, end_at) if is_prime(i))
if __name__ == "__main__":
    print(*exercise57(10,50))
