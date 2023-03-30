#!/usr/bin/python3 
import string
import random
length = int(input("Enter the length : "))
result_pass = ""
if length < 8:
    print("Password Should be atleas 8 characters")
else:
    num_of_chars = random.randrange(1,length)
    num_white_space = random.randrange(1, length-num_of_chars)
    num_up_letters = random.randrange(1, length-num_white_space)
    num_low_letters = length-num_up_letters
    digits = length - num_white_space
    all_char_lower = string.ascii_lowercase
    all_char_upper = string.ascii_uppercase
    white_space = string.punctuation
    nums_ascii = string.digits

    pass_ = random.choices(nums_ascii, k=digits) + random.choices(white_space,k=num_white_space) + random.choices(all_char_lower, k=num_low_letters) + random.choices(all_char_upper, k=num_up_letters) 
    pass_ = random.choices(pass_,k=len(pass_))
    for x in pass_:
        result_pass += x
if len(result_pass) > 0:
    print(result_pass)
else:
    print("Password Not Generated")
