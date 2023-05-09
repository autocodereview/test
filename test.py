# 1から100までの数字を順番に表示し、3の倍数の場合は"Fizz"、5の倍数の場合は"Buzz"、3と5の倍数の場合は"FizzBuzz"と表示するプログラム

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)