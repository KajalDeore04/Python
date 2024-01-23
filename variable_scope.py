# scope - its the region where variable is recognized

name = "Java"                    # global variable

def display():
    name = "Python"               #variable name is declared inside function (local scope)
    print(name)

#print(name)                        #name variable cant be accessed from outside

'''Python follows LEGB rule :
       Local: first local variable is checked if there is any value it is prioritized first
       Enclosing
       global
       built in'''