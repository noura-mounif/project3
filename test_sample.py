def mult_two(a: int, b: int) -> int:

    return a*b


print("Example")
print(mult_two(1, 2))

assert mult_two(3, 2) == 6
assert mult_two(0, 1) == 0

print("The first mission is done! Click 'Check' to earn cool rewards!")
#============================================================
def is_acceptable_password(password: str) -> bool:
    cond1 = len(password) > 6
    return cond1
    


print("Example:")
print(is_acceptable_password("short"))

assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
#=========================================================
def backward_string(val: str) -> str:
    return val[::-1]


print("Example:")
print(backward_string("val"))

assert backward_string("val") == "lav"
assert backward_string("") == ""
assert backward_string("ohho") == "ohho"
assert backward_string("123456789") == "987654321"

print("The mission is done! Click 'Check Solution' to earn rewards!")
#=====================================================
def is_even(num: int) -> bool:
    return num % 2==0
    


print("Example:")
print(is_even(2))

assert is_even(2) == True
assert is_even(5) == False
assert is_even(0) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
#==========================================
def first_word(text: str) -> str:
    words = text.split()
    return words[0]


print("Example:")
print(first_word("Hello world"))

assert first_word("Hello world") == "Hello"
assert first_word("a word") == "a"
assert first_word("greeting from CheckiO Planet") == "greeting"
assert first_word("hi") == "hi"

print("The mission is done! Click 'Check Solution' to earn rewards!")
#==================================================================
def checkio(number: int) -> str:
        
        if not number % 15:
            return "Fizz Buzz"
        elif not number % 5:
            return "Buzz"
        elif not number % 3:
            return "Fizz"
        
        return str(number)


print("Example:")
print(checkio(15))

assert checkio(15) == "Fizz Buzz"
assert checkio(6) == "Fizz"
assert checkio(10) == "Buzz"
assert checkio(7) == "7"

print("The mission is done! Click 'Check Solution' to earn rewards!")
#============================================
def sum_numbers(text: str) -> int:
    result = []
    for i in text.split():
            if i.isdigit():
                result.append(int(i))
    return sum(result)


print("Example:")
print(sum_numbers("hi"))

assert sum_numbers("hi") == 0
assert sum_numbers("who is 1st here") == 0
assert sum_numbers("my numbers is 2") == 2
assert (
    sum_numbers(
        "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
    )
    == 3755
)
assert sum_numbers("5 plus 6 is") == 11
assert sum_numbers("") == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
#===========================================
def checkio(words: str) -> bool:
    count = 0
    for w in words.split():
        if w.isalpha():
            count += 1
            if count == 3:
                return True
        else:
            count = 0
            
    return False


print("Example:")
print(checkio("Hello World hello"))

assert checkio("Hello World hello") == True
assert checkio("He is 123 man") == False
assert checkio("1 2 3 4") == False
assert checkio("bla bla bla bla") == True
assert checkio("Hi") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
#====================================
def is_acceptable_password(password: str) -> bool:

    cond1 = len(password) > 6
    cond2 = any(map(str.isdigit, password))

    return all([cond1, cond2])

   





assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == False
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")