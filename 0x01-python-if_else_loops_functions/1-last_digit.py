#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)
print("The Last digit of {} is {}".format(number, last_digit), e=' ')
if last_digit > 5:
    print("and is greater than 5")
if last_digit == 0:
    print("and is 0")
if last_digit < 6 and last_digit != 0:
    print("and is less than 6 and not 0")
                            
