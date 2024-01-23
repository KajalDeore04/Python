# set - unordered , unindexed collection . no duplicate values

utensils = {"knife","spoon","pan","pan"}
cutlery = {"cup", "plate","pan"}

# utensils.add("bowl")
#
# utensils.remove("knife")
#
# utensils.update(cutlery)          #added new set to the set
#
# dinner_table = utensils.union(cutlery)   #merged both sets in dinner_table
#
# print(utensils.difference(cutlery))      # prints what utensil has that cutlery doesnt


for i in utensils:           #while printing sequence changes everytime and wont print duplicate value
    print(i)


print(utensils.intersection(cutlery))    #prints what is common