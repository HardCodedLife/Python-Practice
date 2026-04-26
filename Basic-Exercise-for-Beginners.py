import sys
from pathlib import Path

def task_1():
    for i in range(10):
        print(f'Current number {i} Previous number {0 if i-1<0 else i-1} Sum: {i + (0 if i-1<0 else i-1)}')

def task_2(sentence: str):
    for i,c in enumerate(sentence):
        if i%2==0:
            print(c)
            
def task_2_better(sentence: str):
    even_of_sentence = sentence[0::2]
    for i in even_of_sentence:
        pass
        #print(i)
    
    for i in range(0, len(sentence), 2):
        print(sentence[i])
        

def remove_chars(characters: str, index: int):
    return characters[index:]

def removing_duplicates_from_a_list(input: list) -> tuple:
    return tuple(set(input))

def list_comparison_and_boolean_logic(input: list) -> bool:
    if input[0] == input[-1]:
        return True
    else:
        return False

def filtering_lists_with_conditional_logic(num_list: list) -> tuple:
    return tuple(filter(lambda x: x%5==0, num_list))
        
def substring_frequency_analysis(input: str, pattern: str) -> int:
    if pattern not in input:
        return 0
    else:
        return input.count(pattern)

def nested_loops_for_pattern_generation(row: int) -> None:
    for i in range(row):
        current = i+1
        for j in range(current):
            print(current,end=" ")
        print("")

def numerical_palindrome_check(number: int) -> bool:
    number = str(number)
    reversed_number = number[::-1]
    if number == reversed_number:
        return True
    else:
        return False
    #left = 0
    #for i in range(len(number)-1,-1,-1):
    #    if number[i] != number[left]:
    #        return False
    #    left += 1
    #return True

def merging_lists_with_parity_filtering(list1: list[int], list2: list[int]) -> list[int]:
    return list(filter(lambda x: x%2!=0, list1)) + list(filter(lambda x: x%2==0,list2))

def integer_digit_extraction_and_reversal(number: int) -> tuple[int, ...]:
    result = []
    if number < 0:
        result.append('-')
        number = abs(number)
    divisor = 10
    while number != 0:
        result.append(number % divisor)
        number //= divisor
    return result

def multi_tiered_income_tax_calculation(income: int) -> float:
    tax = 0
    if income > 20_000:
        tax += (income - 20_000) * 0.2
        income = 20_000
    if income > 10_000:
        tax += (income - 10_000) * 0.1

    return tax

def nested_loops_for_multiplication_tables() -> None:
    for i in range(10):
        for j in range(10):
            print(f"{(i+1)*(j+1):<2}",end=" ")
        print()

def downward_half_pyramid_pattern(rows: int) -> None:
    for i in range(rows,0,-1):
        print("* "*i)

def exponent(base: int, exp: int) -> int:
    result = 1
    if exp == 0:
        return result

    for i in range(exp):
       result *= base
    return result

def check_palindrome_number(number: int) -> bool:
    result = []
    divisor = 10
    while number != 0:
        result.append(number%divisor)
        number //= divisor
    if result == result[::-1]:
        return True
    else:
        return False
    #number = str(number)
    #left = 0
    #right = len(number) - 1
    #for i in range(len(number)//2 + 1):
    #    if number[left] != number[right]:
    #        return False
    #return True
    
def generate_fibonacci_series(terms: int) -> tuple[int, ...]:
    result = [0, 1]
    while len(result) < terms:
        result.append(result[-1] + result[-2])
    return tuple(result)

def check_leap_year(year: int) -> bool:
    if year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4== 0:
        return True
    else:
        return False

def merging_two_dictionaries(dict1: dict, dict2: dict) -> dict:
    for key in dict2:
        dict1[key] = dict2[key]
    return dict1

def finding_common_elements(list_a: list, list_b: list) -> set:
    return set(list_a) & set(list_b)

def odd_even_list_splitter(numbers: list[int]) -> tuple[list[int],list[int]]:
    return [x for x in numbers if x%2 == 0], [x for x in numbers if x%2 != 0]

def word_length_analysis(words: list[str]) -> list[int]:
    return [f"{word} - {len(word)}" for word in words]

def word_frequency_counter(text: str) -> dict[str:int]:
    tmp = {word:0 for word in set(text.split())}
    for word in text.split():
        tmp[word] += 1
    return tmp

def print_alternate_prime_numbers(limit: int) -> list[int]:
    result = [2]
    for i in range(3, limit+1):
        current = 2
        is_prime = True
        while current <= i**0.5:
            if i % current == 0:
                is_prime = False
                break
            current += 1
        if is_prime:
            print(result[-1], end="") if len(result) %2 !=0 else print(", ", end="")
            result.append(i)
    return result

def dictionary_of_squares(numbers: range) -> dict[int:int]:
    return {i: i**2 for i in numbers}

def character_replacer(sentence: str) -> str:
    return sentence.replace(" ","_")

def print_reverse_number_pattern(rows: int) -> str:
    result=""
    for i in range(rows,0,-1):
        for j in range(i,0,-1):
            result += str(j) + " "
        result += "\n"
    return result

def digit_detection_in_strings(sentence: str) -> bool:
    for c in sentence:
        if c.isdigit():
            return True
    return False

def capitalize_first_letter(text: str) -> str:
    return " ".join([w.capitalize() for w in text.split()])

def simple_countdown_timer(start_count: int) -> None:
    import time
    while start_count>0 :
        print(start_count, end=" ", flush = True)
        time.sleep(1)
        start_count -= 1
    print("Blast off!")

def file_create(filename: str | Path):
    with open(filename, "w") as file:
        file.write("Write a program that creates a new text file named notes.txt, ")
        file.write("writes three separate lines of text to it, ")
        file.write("and then reads that file back to display the contents in the console.")

def file_read(filename: str | Path) -> str:
    result=''
    with open(filename, "r") as file:
        result = file.read()
    return result

def external_file_word_counter(filename: str | Path) -> int:
    with open(filename,"r") as file:
        result = file.read()
    return len(result.split())

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def start_engine(self):
        print(f"{self.make},{self.model},{self.year} starting up")

if __name__ == "__main__":
    a = generate_fibonacci_series(15)
    print(a, end="\n---\n")
    a = check_leap_year(2024)
    print(a, end="\n---\n")
    dict1 ={"name": "Alice", "age": 25}
    dict2 = {"city": "New York", "job": "Engineer"}
    a = merging_two_dictionaries(dict1, dict2)
    print(a, end="\n---\n")
    a = finding_common_elements([1,2,3,4,5],[4,5,6,7,8])
    print(a, end="\n---\n")
    a = odd_even_list_splitter([12,7,34,21,5,10,8,3,19,2])
    print(a, end="\n---\n")
    a = word_length_analysis(["apple","banana","cherry","date","elderberry"])
    print(a, end="\n---\n")
    a = word_frequency_counter("apple banana apple cherry banana apple")
    print(a, end="\n---\n")
    print_alternate_prime_numbers(20)
    print("\n---")
    a = dictionary_of_squares(range(1,11))
    print(a, end="\n---\n")
    a = character_replacer("I love coding in Python.")
    print(a, end="\n---\n")
    a = print_reverse_number_pattern(5)
    print(a, end="\n---\n")
    a = digit_detection_in_strings("Python3")
    print(a, end="\n---\n")
    a = capitalize_first_letter("hello world from python")
    print(a, end="\n---\n")
    simple_countdown_timer(5)
    print("", end="\n---\n")

    notes = Path("notes.txt")
    file_create(notes)
    a = file_read(notes)
    print(a, end="\n---\n")
    notes.unlink()

    simple_file = Path("simple.txt")
    with open(simple_file,"w") as file:
        file.write("Coding is the language of the future.")
    a = external_file_word_counter(simple_file)
    print(a, end="\n---\n")
    simple_file.unlink()

    a = Car("Toyota", "Altis", "2026")
    a.start_engine()

