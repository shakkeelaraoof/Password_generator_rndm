import random 

uppercase_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letter = uppercase_letter.lower()
digits = "0123456789"
symbols = " }{[]()-*;:'?,.!@#$%^& "

upper, lower, nums, syms = True, True, True, True
#Here the password will print only without Symbols So we need make that 'True'
 
all = ""

if upper:
    all += uppercase_letter

if lower:
    all += lowercase_letter

if nums:
    all += digits

if syms:
    all += symbols

length = 20   #Number of Characters in the password
amount = 10   #Number of Password Generated

#-----------------------
#if we are using this code we wil get 10 passwords and it will be same at all time there will be no change(It will show same)
#same = "neuralnines"
#random.seed(same)

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)








