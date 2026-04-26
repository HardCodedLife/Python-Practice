from collections.abc import Generator
def is_prime(N: int) -> bool:
    if N <= 1:
        return False
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            return False
    else:
        return True

def split_number(N: int) -> tuple[int, ...]:
    result = []
    while N > 0:
        result.append(N%10)
        N //= 10
    else:
        return result[::-1]
def reverse_number(N: int) -> int:
    result = 0
    for i in split_number(N)[::-1]:
        result = result*10 + i
    else:
        return result

def exe1() -> tuple[int, ...]:
    result = []
    while (i:=len(result)) < 10 :
        result.append(i+1)
    return result

def exe2() -> tuple[int, ...]:
    return [x for x in range(-10, 0)]

def exe3() -> None:
    for i in range(5):
        print(i)
    else:
        print("Done!")

def exe4(N: int) -> int:
    sum = 0
    for i in range(N + 1):
        sum += i
    else:
        return sum

def exe5(N: int) -> Generator[int, None, None]:
    return (N*(i+1) for i in range(10))

def exe6(N: int) -> Generator[tuple[int,int], None, None]:
    return ((x, x**3) for x in range(1,N+1))

def exe7(numbers: list[int]) -> None:
    for e in numbers:
        if e > 500:
            break
        if e > 150:
            continue
        if e % 5 == 0:
            print(e)

def exe8(list1: list[int], target: int) -> int:
    return list1.count(target)

def exe9(my_list: list[int]) -> tuple[int, ...]:
    return tuple(my_list[1::2])

def exe10(list1: list[int]) -> tuple[int, ...]:
    return tuple(list1[::-1])

def exe11(original: str) -> str:
    result = ""
    for c in original:
        result = c + result
    else:
        return result
def exe12(target: str) -> tuple[int, int]:
    return sum([1 for e in target if e.lower() in ["a","e","i","o","u"]]), sum([1 for e in target if e.lower() not in ["a","e","i","o","u",' ']])

def exe13(N: int) -> int:
    return len(split_number(N))

def exe14(N: int) -> int:
    result = 0
    for i in split_number(N)[::-1]:
        result = result*10 + i
    else:
        return result

def exe15(N: int) -> tuple[int,int]:
    temp = split_number(N)
    return max(temp), min(temp)

def exe16(N: int) -> bool:
    return True if N == reverse_number(N) else False

def exe17(N: int) -> int:
    result = 1
    for i in range(N):
        result *= i+1
    else:
        return result
def exe18(N: int) -> tuple[int, ...]:
    result = [N]
    while N != 1:
        if N%2 == 0:
            N = N//2
        else:
            N = N * 3 + 1
        result.append(N)
    else:
        return result
def exe19(N: int) -> bool:
    sum_num = 0
    for i in split_number(N):
        sum_num += i**3
    else:
        return True if sum_num==N else False
def exe20() -> str:
    result = ""
    for i in range(5):
        for j in range(i+1):
            result += str(j+1)+' '
        result += '\n'
    else:
        return result
def exe21(N: int) -> str:
    result = ''
    for i in range(5,0,-1):
        for j in range(i,0,-1):
            result += str(j) + ' '
        result += '\n'
    else:
        return result
def exe22(N: int) -> tuple[int, ...]:
    result = []
    for i in range(1, N+1, 2):
        result.append(i)
    else:
        return tuple(result)
def exe23(N: int) -> None:
    start = 65
    for i in range(N):
        for j in range(i+1):
            print(chr(start),end=" ")
        print()
        start += 1
    else:
        return None
def exe24(size: int) -> None:
    for i in range(size):
        for j in range(size):
            if i==0 or i==size-1 or j==0 or j== size-1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
    else:
        "Done!"
def exe25(rows: int) -> None:
    for i in range(rows):
        print('* '*(i+1))
    for i in range(rows-1,0,-1):
        print('* '*i)
def exe26() -> None:
    for i in range(10):
        for j in range(10):
            print((i+1)*(j+1), end="\t")
        print()
def exe27(target: list[int]) -> tuple[int, ...]:
    total = 0
    return ( (total:= total + i) for i in target)
def exe28(scores: dict[str,int], threshold: int) -> dict[str,int]:
    return {k:v for k,v in scores.items() if v>threshold}
def exe29(list_a:list[int],list_b:list[int])->tuple[int,...]:
    return (e for e in list_a if e in list_b)
def exe30(original: list[int])->tuple[int, ...]:
    result = []
    for e in original:
        if e not in result:
            result.append(e)
    else:
        return tuple(result)
def exe31(original: list[int])->tuple[int, ...]:
    return tuple([i for i in original if i%2 == 0] + [i for i in original if i%2 != 0] )
def exe32(nums: list[int], k:int) -> tuple[int, ...]:
    nums[k:] + nums[:k]
    result = []
    for i,e in enumerate(nums):
        if i+k >= len(nums):
            i = (i+k) % len(nums)
        else:
            i += k
        result.append(nums[i])
    else:
        return result
def exe33(text: str) -> dict[str,int]:
    words = text.split()
    result = {word:0 for word in set(words)}
    for word in words:
        result[word] += 1
    else:
        return result
def exe34(n_terms:int)->tuple[int, ...]:
    result = [0,1]
    one,two = 0,1
    for i in range(n_terms-2):
        current = one + two
        result.append(current)
        one = two
        two = current
    return tuple(result)
def exe35(num: int) -> tuple[int, ...]:
    result = []
    for i in range(1, num//2+1):
        if num % i == 0:
           result.append(i)
    else:
        return result
def exe36(binary_str: str) -> int:
    result = 0
    power = 0
    for i in binary_str[::-1]:
        result += int(i) * 2**power
        power += 1
    else:
        return result
def exe37(start:int,end:int)->tuple[int,...]:
    result = []
    for i in range(start,end):
        if is_prime(i):
            result.append(i)
    else:
        return tuple(result)
def exe38(number_of_terms:int)->int:
    result = 0
    for i in range(number_of_terms):
        result += int('2'*(i+1))
    else:
        return result
def exe39(nested_list: list[list[int]])->tuple[int, ...]: 
    return (e for l in nested_list for e in l)

def exe40(matrix: list[list[int]], target:int)->Generator[tuple[int,int], None,None]:
    return ((row, column) for row,l in enumerate(matrix) for column,e in enumerate(l) if e == target)

if __name__ == "__main__":
    #print(*exe1(), sep = "\n")
    #print(*exe2(), sep = "\n")
    #exe3()
    #print(exe4(10))
    #print(*exe5(2), sep = "\n")
    #print(*(f"Current Number is : {e[0]} and the cube is {e[1]}" for e in exe6(6)), sep = "\n")
    #exe7([12,75,150,180,145,525,50])
    #print(exe8([10,20,10,30,10,40,50], 10))
    #print(exe9([10,20,30,40,50,60,70,80,90,100]))
    #print(exe10([10,20,30,40,50]))
    #print(exe11("Python"))
    #print(f"Vowels: {(temp:=exe12('Loops are Fun!'))[0]}\nConsonants: {temp[1]}")
    #print(f"Total digits are: {exe13(75869)}")
    #print(exe14(76542))
    #print(f"Largest digit: {(temp:=exe15(75869))[0]}\nSmallest digit: {temp[1]}")
    #print("Yes" if exe16(122) else "No")
    #print(exe17(5))
    #print(*exe18(6))
    #print("Yes" if exe19(153) else "No")
    #print(exe20())
    #print(exe21(5))
    #print(*exe22(20))
    #exe23(5)
    #exe24(5)
    #exe25(5)
    #exe26()
    #print("Cumulative Sum: ", *exe27([1,2,3,4]))
    #print("Passing Students: ", exe28({"Alice": 85, "Bob": 70, "Charlie": 95, "David": 60}, 75))
    #print('Common elements: ', *exe29([1, 2, 3, 4, 5],[4, 5, 6, 7, 8]))
    #print(exe30([1,2,2,3,4,4,4,5]))
    #print(f"Segregated List: {exe31([1,2,3,4,5,6])}")
    #print(f"Rotated List: {exe32([1,2,3,4,5],2)}")
    #print(exe33("apple banana apple orange banana apple"))
    #print(*exe34(10))
    #print(sum(exe35(28)) == 28)
    #print(exe36("1101"))
    #print(exe37(25,50))
    #print(exe38(5))
    #print(*exe39([[10, 20], [30, 40], [50, 60]]))
    print(*exe40([[10, 20], [30, 40], [50, 60]],30))
