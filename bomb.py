import re
def wire3(colors):
    i = 0
    for wire in colors:
        colors[i] = wire.lower()
        i+=1
    i = 0
    for wire in colors:
        wire = wire.lower()
        if wire == 'r':
            i = 1
    if i == 0:
        print('second')
    else:
        if colors[2].lower() == 'w':
            print('last')
        else:
            i = 0
            for wire in colors:
                if wire.lower() == 'bl':
                    i+=1
            if i > 1:
                result = len(colors) - 1 - colors[::-1].index('bl')
                if result == 0:
                    print('first')
                elif result == 1:
                    print('second')
                else:
                    print('last')
            else:
                print("last")

def wire4(colors):
    i=0
    for wire in colors:
        colors[i] = wire.lower()
        i+=1
    red=0
    blue=0
    yellow=0
    for wire in colors:
        if wire == "r":
            red+=1
        elif wire == "bl":
            blue+=1
        elif wire == "y":
            yellow+=1
    if red > 1 and int(serial[5])%2 != 0:
        result = len(colors) - 1 - colors[::-1].index('r')
        if result == 0:
            print('first')
        elif result == 1:
            print('second')
        elif result == 2:
            print('third')
        else:
            print('last')
    elif colors[3] == 'y' and red == 0:
        print("first")
    elif blue == 1:
        print("first")
    elif yellow > 1:
        print("last")
    else:
        print("first")
    
def wire5(colors):
    i=0
    for wire in colors:
        colors[i] = wire.lower()
        i+=1
    red = 0
    yellow = 0
    i = 0
    for wire in colors:
        if wire == "r":
            red+=1
        elif wire == "y":
            yellow+=1
        elif wire == "b":
            i=1
    if i==1 and int(serial[5])%2!=0:
        print("fourth")
    elif red == 1 and yellow>1:
        print("first")
    elif i == 0:
        print("second")
    else:
        print("first")

def wire6(colors):
    i=0
    for wire in colors:
        colors[i] = wire.lower()
        i+=1
    yellow=0
    white=0
    i=0
    for wire in colors:
        if wire == "w":
            white+=1
        elif wire == "y":
            yellow+=1
        elif wire == "r":
            i=1
    if yellow == 0 and int(serial[5])%2!=0:
        print("third")
    elif yellow == 1 and white >1:
        print("fourth")
    elif i==0:
        print("last")
    else:
        print("fourth")

def buttonMod():
    color = input("Color of button? (Input first letter of color):\n")
    col = re.compile("[rRwWyYbB]")
    val = re.match(col,color)
    while not val:
        color = input("Error, enter a valid color:\n")
        color = color.lower()
        val = re.match(col,color)
    text = input("Text on button?:\n")
    text = text.lower()
    v = 0
    while v != 1:
        if text == "detonate" or text == "abort" or text == "press" or text == "hold":
            v = 1
        else:
            text = input("Error, input a valid word:\n")
            text = text.lower()
    frk = 0
    car = 0
    for ind in list(indicators):
        if ind == "frk":
            frk = 1
        elif ind == "car":
            car = 1
    if color=="b" and text == "abort":
        print("Hold and release with number in any position\nBlue=4\nWhite=1\nYellow=5\nOther=1")
    elif battery >1 and text == "detonate":
        print("Press and immediate release")
    elif color == "w" and car == 1:
        print("Hold and release with number in any position\nBlue=4\nWhite=1\nYellow=5\nOther=1")
    elif battery>2 and frk == 1:
        print("Press and immediate release")
    elif color == "y":
        print("Hold and release with number in any position\nBlue=4\nWhite=1\nYellow=5\nOther=1")
    elif color == "r" and text == "hold":
        print("Press and immediate release")
    else:
        print("Hold and release with number in any position\nBlue=4\nWhite=1\nYellow=5\nOther=1")
    choose()

def serialValid(serial):
    while len(serial) is not 6:
        if len(serial) < 6:
            serial = input("Error, serial is too short:\n")
        else:
            serial = input("Error, serial is too long:\n")
    while not serial[5].isdigit():
        serial = input("Error, serial must end in a number:\n")

def batteryValid(battery):
    valid = 0
    while not valid:
        try:
            int(battery)
            if battery >= 0:
                valid=1
            else:
                battery = input("Error, number must be positive:\n")
        except ValueError:
            battery = input("Error, number must be an integer:\n")

def wireMod():
    num = input("Number of wires?\n")
    while num > 6 or num < 3:
        num = input("Error, number must be between 3 and 6:\n")
    wires = input("Order of Wires (using the first letter only, except for Black = k, Blue = b):\n")
    wires = wires.split()
    while len(wires) != num:
        wires = input("Error, incorrect number of wires:\n")
        wires = wires.split()
    wirecol = re.compile("[rRwWyYbBkK]")
    v = 0
    while v == 0:
        for w in wires:
            color = re.match(wirecol,w)
            if color:
                v = 1
            else:
                v = 0
        if v == 0:
           wires = input("Error, invalid color detected:\n")
           wires = wires.split()
           while len(wires) != num:
               wires = input("Error, incorrect number of wires:\n")
               wires = wires.split()
        else:
            break        
    if num is 3:
        wire3(wires)
    elif num is 4:
        wire4(wires)
    elif num is 5:
        wire5(wires)
    elif num is 6:
        wire6(wires)
    else:
        print("Something went wrong, try again")
    choose()

def module(num):
    if num is 1:
        wireMod()
    elif num is 2:
        buttonMod()
    elif num is 0:
        print("Complete")
        return
        
def choose():
    choice = input("Please enter module selection:\n1)\tWires\n2)\tButton\n3)\tSymbols\n0)\tExit\n")
    choice = int(choice)
    module(choice)

serial = input("Enter the serial number:\n")
serialValid(serial)
battery = input("Enter number of batteries:\n")
batteryValid(battery)
ind= input("Please enter all LIT indicators:\n")
indicators = ind.split()
choose()
