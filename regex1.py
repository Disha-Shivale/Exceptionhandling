import re
s = "Hello from Python, This is Reg Expression"
i = re.search("^Hello", s)
# ^Starts with
if (i):
    print("String Match!")
else:
    print("No match")

#Example 2

i = "Hello from Python"
print()
#Find all lower case characters alphabetically between "a" and "m":
x = re.findall("[a-z]", i)
print(x)
print()


#Example 3
s = "hello from python"
#Check if the string ends with 'world':
i = re.findall("on$", s)
if (i):
    print("String Match")
else:
    print("No match")