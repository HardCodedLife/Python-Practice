import random
def exercise55():
    answer = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    count = 10
    guess = -1
    while answer != guess and count > 0:
        try:
            guess = int(input(f"({count} left) Enter guess: "))
            print("Higher!" if guess < answer else "Lower!" if guess > answer else f"Correct! The number was {guess}.")
        except Exception:    
            print("Invalid input, try again.")
        count -= 1
    if answer != guess:
        print(f"Answer: {answer}")
if __name__ == "__main__":
    exercise55()
