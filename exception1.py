try:
    print(i + j)
except:
    print("Value not defined")

print("Hello from Python")
print()

#Variable not defined exception
try:
    print(i + j)
except NameError:
    print("Variable i,j not defined")
except:
    print("Proble in your code...")

#Else keyword in Exception
print()
try:
    print("Hello from Python")
except:
    print("Problem in your code")
else:
    print("Code is running well")