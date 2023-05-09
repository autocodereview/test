import math, random

def get_input():
    try:
        num = int(input("Enter a number: "))
        if num < 1 or num > 10:
            raise ValueError
        return num
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 10.")
        return get_input()

num = get_input()
numbers = [random.randint(1, 10) for _ in range(num)]
result = list(map(lambda x: math.sqrt(x), numbers))
print(result)