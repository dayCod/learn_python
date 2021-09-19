# How to accessing file in python, in this case using .txt format
# FILE HANDLING

# "r" -> Default value. Opens a file for reading, error if the file does not exist (read)
# "a" -> Opens a file for appending, creates the file if it does not exist (append)
# "w" -> Opens a file for writing, creates the file if it does not exist (write)
# "x" -> Creates the specified file, returns an error if the file exists (create)

file = open("C:/LEARN PYTHON/learning_python/file_handling/file.txt", "r")
print(file.readable()) #True
print(file.read()) #return value of file.txt

# how to loop an list/tuples/dict and how to loop a value of the file
# FOR LOOP

# LIST
transportation = ["car", "bicycle", "motorcycle", "train", "plane", "boat"]
for x in transportation:
    print(x)

# TUPLES
transportations = ("car", "bicycle", "motorcycle", "train", "plane", "boat")
for x in transportations:
    print(x)

# DICT 
foods = {"menu" : ["Fried Rice", "French Fries", "Fried Cassava", "Spaghetti"], "price" : [20000, 17000, 15000, 25000]}
menus = foods["menu"]
for i in menus:
    print(i)
prices = foods["price"]
for l in prices:
    print(l)

# WHILE LOOP
number = 0
while number <= 10:
    print(number)
    number += 1


