import random

x = random.randint(1,6)       #gives random number betn 0-6
print(x)

y = random.random()                 #below 0
print(y)

mylist = ["rock","paper","scissor"]
z = random.choice(mylist)
print(z)                              #random elements in the list

cards = [1,2,3,4,5,6,7,8,9,"j","q","k","a"]
random.shuffle(cards)
print(cards)                           #Shuffle gives random order