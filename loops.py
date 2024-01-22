# two types - for loop and while loop or nested 

#1.FOR LOOP
#iterating over a string
name = "Kajal"
for i in name:
    print(i)         #prints in column / each word on new line
    #print(i,end=", ") #prints in one line separated by commas


#iterate over a list
colours = ["Red","Yellow","Black","Brown"]    
for a in colours:
    print(a , end = " ")
    for i in a:
        print(i)






#RANGE - it is a function
for k in range(5):       #in range 5 means from 0 to 4
    print(k)    

for k in range(1,9):     # starts from 1 til 8
    print(k)

for k in range(1,5,2):    #starts from 1 ends at 4 but prints elements only after incrementing it by 2 
    print(k)              #o/p= 1 3










#2.While loops
print("Using While Loop")  


i = 0

while(i<3):
    print(i)    
    i = i + 1

count = 5                 #reverse loop
while(count>0):
    print(count)
    count = count - 1


b = int(input())
while(b<=10):
    b = int(input("Enter Value for b"))
    print(b)
else:                                      # runs when condition becomes false
    print("This is else part")




# do {
  # loop body;
# }while(condition);
    

#emulate do while loop in python
while True:
    number = int(input("Enter a positive number: "))
    print(number)
    if not number > 0:
       break
 
'''
This loop takes the user’s input using the built-in input() function. The input is then converted into an integer number using int(). If the user enters a number that’s 0 or lower, then the break statement runs, and the loop terminates.

At times, you’ll encounter situations where you need a guarantee that a loop runs at least once. In those cases, you can use while and break as above.
'''        