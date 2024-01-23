# stores all elements in single variable  just like array

food = ["pizza", "pudding", "sandwich"]

print(food[1])   #accessing particular element

food[0] = "sushi"  #updating element

food.append("mac n chees")   #adding element to the list at last position

food.remove("sandwich")       #removed element

food.pop()  #removes last element

food.insert(0,"burger") #inserts element at given index

food.sort()        #will sort alphabetically

food.clear()    # delete all elements

for i in food:   #printing all elements using loop
    print(i)



# 2D list - list of list
animals = ["tiger","lion","zebra"]
birds = ["pigeon","crow","eagle"]
insects = ["grasshoper","dragonfly","ant"]

living_things = [animals,birds,insects]

print(living_things)        #prints all 9

print(living_things[0])     # prints first 3

print(living_things[0][0])   # prints only the first ever element
