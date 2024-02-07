marks = [12,56,45,1,6]

"""
index = 0
for mark in marks:
    print(mark)
    if(index == 3):
        print("WOW!!")
    index += 1
"""


for index, mark in enumerate(marks):
    print(mark)
    if index == 3:
        print("WOW!!")
