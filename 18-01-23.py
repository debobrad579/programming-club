from random import randint
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
    's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
special_characters = ["@", "$", "!", "#", "%", "&", "(", ")", "?", "/"]

length = int(input("Input the length of the password: "))

password = ""

uppercase_count = 0
special_count = 0

for _ in range(length):
    num = randint(0, len(letters + special_characters) - 1)
    char = (letters + special_characters)[num]
    
    if char in letters:
        char = char.upper() if randint(0, 1) else char.lower()
    
    if char in [i.upper() for i in letters]:
        uppercase_count += 1
    
    if char in special_characters:
        special_count += 1
        
    password += char

while (not special_count) or (not uppercase_count):
    if not special_count:
        num = randint(0, length - 1)
        if password[num] in [i.upper() for i in letters]:
            uppercase_count -= 1
        special_count += 1
        password = list(password)
        password[num] = special_characters[randint(0, len(special_characters) - 1)]
        password = "".join(password)
    
    if not uppercase_count:
        while True:
            try:
                num = randint(0, length - 1)
                if password[num] in special_characters:
                    special_count -= 1
                uppercase_count += 1
                password = list(password)
                password[num] = password[num].upper()
                password = "".join(password)
                break
            except: pass

print(f"The password is: {password}")
