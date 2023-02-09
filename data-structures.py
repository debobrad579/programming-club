integer = 2
floating_point = 2.5
boolean = True or False
tuple1 = (1, 2, 3, 4, "hi")

months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "Augest",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

month = input("Input a month (in numeric form): ")
print(months[int(month)])

set1 = {1, 2, 3, 4, 4}
print(set1)
set1.add(5)
print(set1)

array = [1, 2, 3, 4]
tuple1 = (1, 2, 3, 4)
string = "1234"

print(array[0])
print(tuple1[1])
print(string[2])

set2 = {"January", "january", "Jan", "jan"}
value = input("Input a month (in written form): ")

if value in set2:
    print("Value is in the set")
else:
    print("Value is not in the set")

# String Operations
string = "Hello, world!"
upper = string.upper()
lower = string.lower()
print(upper, lower)
count = string.count("e")
print(count)
string = string.replace(" ", "")
print(string)
string_array = string.split(",")
print(string_array)
joined_string = ", ".join(string_array)
print(joined_string)
print(len(string))
