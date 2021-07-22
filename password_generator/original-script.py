#import some libraries
#we're using random.sample module here. This to ensure characters are not being repeated
#string module contains anumber of useful constants, classes, and a number
import random
import string

#greet the user
print("hello, Welcome to Passwords Generator!")

#asking the user the length of the password.
length = int(input('\nEnter the length of password: '))

#defining some data
#we'll make use of string module for the same time
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

#combining and storing data
all = lower + upper + num + symbols

#we'll make use of random module to generate the password
temp = random.sample(all, length)
#joining all together at the end
password = "".join(temp)

#depending on need
#if you just need lower + num + symbols, then just use code below


"""

all = string.ascii_lowercase + string.digits + string.punctuation
pass = "".join(random.sample(all, length))
"""

#finally, let's print the password
print(password)