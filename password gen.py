# Modules Imported
import random
import string

# Character sets defined
low = list(string.ascii_lowercase)
up = list(string.ascii_uppercase)
digits = list(string.digits)
specials = list("!@#$%^&*-_=+;:,.?/")

# Shuffling character sets
random.shuffle(low)
random.shuffle(up)
random.shuffle(digits)
random.shuffle(specials)

# Dividing the password length into 4 equal parts
def divider(number):
    part1 = round(number * 0.25)
    part2 = round(number * 0.25)
    part3 = round(number * 0.25)
    part4 = round(number * 0.25)
    return [part1,part2,part3,part4]


def passwordGenerator():
    # Input taken from user
    password = []
    while True:
        s = input("Enter the number of characters for the password: ")
        try:
            number = int(s)
            if number <= 2:
                print("Minimum length of Password is 3, Please re-enter your desired value.")
                continue
        except ValueError:
            print("Please enter an integer digit only.")
            continue
        break
    parts = divider(number)
    # print(parts)
    p1(password,parts[0])
    p2(password,parts[1])
    p3(password,parts[2])
    p4(password,parts[3])
    if(len(password) < number) :
        n = number - len(password)
        for i in range(n):
            m = random.randint(1,4)
            # print(m)
            if m == 1:
                p1(password,parts[0])
            if m == 2:
                p2(password,parts[1])
            if m == 3:
                p3(password,parts[2])
            if m == 4:
                p4(password,parts[3])
    else:
        n = len(password) - number
        for i in range(n):
            password.remove(password[-1])
            # print(password)
    random.shuffle(password)
    passcode = "".join(password)
    return passcode

def p1(password,part1):
    for i in range(part1):
        password.append(random.choice(low))
        # print(password)

def p2(password,part2):
    for i in range(part2):
        password.append(random.choice(up))
        # print(password)

def p3(password,part3):
    for i in range(part3):
        password.append(random.choice(digits))
        # print(password)

def p4(password,part4):
    for i in range(part4):
        password.append(random.choice(specials))
        # print(password)

choice = "Y"
while choice == "Y":
    print(f"Password is : {passwordGenerator()}")
    while True:
        choice = input("Do you want to regenerate the password? (Y/N): ").strip().upper()
        if choice in ("Y", "N"):
            break
        print("Please answer with Y or N.")
