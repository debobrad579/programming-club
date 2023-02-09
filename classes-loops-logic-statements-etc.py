# 11-01-23
import time

# Class_Class - incorrect
# ClassClass - correct

# Classes
class Building:
    def __init__(self, dimentions, label):
        self.dimentions = dimentions
        self.label = label
    
    def __str__(self):
        return f"{self.label} {self.dimentions}"
    
    def __int__(self):
        return self.dimentions[0]
    
    def calculate_volume(self):
        return self.dimentions[0] * self.dimentions[1] * self.dimentions[2]


def square_numbers(x = 2):
    x ** 2
print(square_numbers())

# squareNumbers - not in Python


building1 = Building((20, 20, 20), "building1")
# print(building1.calculate_volume())
# print(int(building1))


class School(Building):
    def __init__(self, dimentions, label, num_of_students):
        super().__init__(dimentions, label)
        self.num_of_students = num_of_students

print("\"String\"\nString")

school1 = School((1, 1, 1), "HDCH", 400)
# print(school1, school1.num_of_students)

# Logic Statements
num1 = 1
num2 = 2
num3 = 3

if num1 < num2 < num3:
    print("True")
elif num3 < num2:
    print("Ha")
else:
    print("False")

if num4 := 4:
    pass
    #print("Hello, world!")
    #print(num4)
    
if True ^ False ^ False:
    print("Yes")
    
"""
num5 = None
if num1 == 1:
    num5 = 5
else:
    num5 = 6
"""

num5 = 5 if num1 == 1 else 6
print(list(i for i in range(5, 20)))

dictionary = {
    0: "Brady", 
    1: "David", 
    2: "Luke", 
    3: "Sam", 
    4: "Lydia",
    5: "Blyleven",
    6: "Caleb"
}

for key in dictionary:
    print(key, dictionary[key])

"""
def square(x):
    return x ** 2
"""

square = lambda x: x ** 2
print(square(8))

# > < >= <= == != := and or

"""
This is a comment block
Line 2
"""


while num2:
    break
    num2 = int(input("Input a number: "))
    print(num2)
    if num2 == 2:
        break
else: # <---
    print("Exited")


"""
if (num2) {
    do stuff
    GOTO 65
} else { <--- Same else statement as above
    do other stuff
}
"""

for _ in range(5):
    print("Looping")
    # time.sleep(2)
    
arr1 = [1, 2, 3, 4, 5, 6]

"""
for (i=0; arr1.length; i++) {
    console.log(arr1[i])
}
"""

for i in arr1:
    print(i ** 2)
    
for index, item in enumerate(arr1):
    print(item ** 2, index)
