for i in range(12):
    if(i == 5):
        continue                          #skipped the fifth iteration i.e 6
    if (i == 10):
        break                              # i started from 0 hence loop stopped prematurely on 11th
    print(" 5 X ", i+1 ,"=", 5*(i+1))
