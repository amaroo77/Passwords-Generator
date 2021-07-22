import random
import string
import time

#greet the user
print("\nhello, Welcome to Passwords Generator!")
print("Let's generate some passwords ^^")

nOfPasswd = int(input('\nHow many passwords you want to generate? (Default 10): ') or "10")
print("")

#asking the user the length of the password.
length = int(input('\nEnter the length of password (default 16): ') or "16")
print("")


#defining some data
#we'll make use of string module for the same time
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

#combining and storing data
all = lower + upper + num + symbols

a = 0
while 1:

    #we'll make use of random module to generate the password
    temp = random.sample(all, length)
    a += 1
    password = "".join(temp)
    #Holding 1 second
    time.sleep(1)
    #print the password
    print(a, " ", password)
    #repeat

    #print the last message
    if a == nOfPasswd:
        print("\nThat's all. Thank You")
        print("-Created by NaOH-")
        break
