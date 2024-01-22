#like switch case

x = int(input(" enter value of x: "))

match x:

    case 0:
        print("You chose case 0")                 #break statement is not mandotory like in java or c
    case 1:
        print("You chose case 2")
    case 2 if x!=15:
        print("case with condition and if not equals to 15")    
    case _ if x !=14:
        print("case with condition")
    case _: 
        print(" this is default case")            #Works as an else part and run if cases number doesnt match, this has to be at last of throws an error 
                                           
















