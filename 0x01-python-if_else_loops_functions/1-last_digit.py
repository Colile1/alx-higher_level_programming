#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    sign = -1
else:
    sign = 1

str_number = str(number)
last_digit = str_number[len(str_number)-1]
last_int = int(last_digit)*sign
if int(last_int) > 5:
    msg = "and is greater than 5"
elif last_int == 0:
    msg = "and is 0"
else:
    msg = "and is less than 6 and not 0"
print("Last digit of", number, "is", last_int, msg)
