
a = input("Enter Number: ")
print("Multiplication table of {} is:".format(a))

try:
    for i in range(1,11):
        print(f"{int(a)} X {int(i)} = {int(a)*i}")

except Exception as e:         #catches the error
    print(e)                   #prints the error
    print("Sorry")             #or we can print any other msg

finally:
    print("Using finally and will run anyways") #runs even if error or not






try:
    num = int(input("Enter Integer: "))
    a = [6,3]
    print(a[num])
except ValueError:
    print("Entered number is not int")  #handles specific error
except IndexError:
    print("Index Error")





#Custom Error

a = int(input("Enter Number betn 5-9"))

if a<5 or a>9:
    raise ValueError("Number between 5-9")    #raises mentioned error checking condition and prints mentioned msg