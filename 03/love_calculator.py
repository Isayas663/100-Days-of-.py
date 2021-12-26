#this is a game to check if you are compattible with your girl 
print("Welcome to the love calculator!!!")

name1 = input("what's your name? ")
name2 = input("what's their name? ")


names= name1.lower() + name2.lower()

local = names.count('t')
total = local
local = names.count('r')
total += local 
local = names.count('u')
total += local 
local = names.count('e')
total += local 

local2 = names.count('l')
total2 = local2
local2 = names.count('o')
total2 += local2 
local2 = names.count('v')
total2 += local2 
local2 = names.count('e')
total2 += local2 

total*=10
final = total + total2

if (final <=10) or (final >=90):
	print(f"Your score is {final}, you go together like coke and mentos.")
elif (final<=50) and (final>=40):
	print(f"Your score is {final}, you are alright together.")
else:
	print(f"your score is {final}.")