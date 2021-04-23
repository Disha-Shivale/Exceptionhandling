#Print pyramid pattern using stars

for i in range(0, 5):
    for j in range(0, i + 1):
        print("* ", end="")
    print()

#Example 2
def pypart(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
n = 5
print()
pypart(n)

