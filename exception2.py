#Finally example
try:
    print(i + j)
except NameError:
    print("Variable not defined")
finally:
    print("This line is always executed")

#Throw an exception
print()
x = int(input("Enter number"))
if x < 10:
    raise Exception("Value must be above 10")
