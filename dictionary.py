# Dictionary - changable , unordered collection. has unique key and value pairs
#               fast coz uses hashing , can access value quickly

capitals = {'USA':'Washington DC',
            'India':'Delhi',
            'China':'Beijing'}

capitals.update({'Germany':'Berlin'})    #adds new to dict

capitals.update({'USA':'LA'})              # changes value

capitals.pop('China')                     #removes given

print(capitals['India'])       #instead of indx we use key to access the value

print(capitals.get('Japan'))     #tries to find it in the dict

print(capitals.keys())         #prints only the keys

print(capitals.values())         #prints only the values

print(capitals.items())         #prints all the pairs

for key,value in capitals.items():    #prints as a normal list
    print(key,value)
