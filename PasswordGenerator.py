# Here we create a password generator
import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}( *;/,_-"


all = lower + upper + numbers + symbols

length = 16

Password = "".join(random.sample(all,length))

print(Password)