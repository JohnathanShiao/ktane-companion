import re
import numpy as np

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
        print("Hold and release with number in any position\nBlue=4\nWhite=1\nYellow=5\nOther=1\n")
    elif battery >1 and text == "detonate":
        print("Press and immediate release")
    elif color == "w" and car == 1:
        print("Hold and release with number in any position\nBlue=4\nWhite=1\nYellow=5\nOther=1\n")
    elif battery>2 and frk == 1:
        print("Press and immediate release")
    elif color == "y":
        print("Hold and release with number in any position\nBlue=4\nWhite=1\nYellow=5\nOther=1\n")
    elif color == "r" and text == "hold":
        print("Press and immediate release")
    else:
        print("Hold and release with number in any position\nBlue=4\nWhite=1\nYellow=5\nOther=1\n")
    choose()

def serialValid():
    global serial
    while len(serial) is not 6:
        if len(serial) < 6:
            serial = input("Error, serial is too short:\n")
        else:
            serial = input("Error, serial is too long:\n")
    while not serial[5].isdigit():
        serial = input("Error, serial must end in a number:\n")

def batteryValid():
    global battery
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

def indicatorValid():
    global indicators
    valid = 0
    if len(indicators) == 0:
        valid = 1
    while not valid:
        for led in indicators:
            if len(led) != 3:
                valid = 0
                indicators = input("Error, input valid indicators:\n")
                indicators = indicators.split()
                break
            else:
                valid = 1

def checkVowel():
    vowel = re.compile("[aAeEiIoOuU]")
    for c in serial:
        found = re.match(vowel,c)
        if found:
            return 1
    return 0     

def simonValid(sequence):
    color = re.compile("[rygb]")
    for c in sequence:
        valid = re.match(color,c)
        if not valid:
            return 0
    return 1

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

def simonMod():
    while True:
        color = input("What is the flashing pattern? (first letter, seperated by a space):\n")
        color = color.lower()
        color = color.split()
        valid = simonValid(color)
        while valid == 0:
            color = input("Error, enter valid color(s):\n")
            color = color.lower()
            color = color.split()
            valid = simonValid(color)
        strike = input("Number of strikes:\n")
        v = 0
        while not v:
            try:
                int(strike)
                if strike >= 0 and strike < 3:
                    v=1
                else:
                    strike = input("Error, number must be between 0 and 2:\n")
            except ValueError:
                strike = input("Error, number must be an integer:\n")
        vowel = checkVowel()
        for c in color:
            if vowel:
                if strike == 0:
                    if c == "b":
                        print("Red\n")
                    elif c == "r":
                        print("Blue\n")
                    elif c == "g":
                        print("Yellow\n")
                    else:
                        print("Green\n")
                elif strike == 1:
                    if c == "b":
                        print("Green\n")
                    elif c == "r":
                        print("Yellow\n")
                    elif c == "g":
                        print("Blue\n")
                    else:
                        print("Red\n")
                else:
                    if c == "b":
                        print("Red\n")
                    elif c == "r":
                        print("Green\n")
                    elif c == "g":
                        print("Yellow\n")
                    else:
                        print("Blue\n")
            else:
                if strike == 0:
                    if c == "b":
                        print("Yellow\n")
                    elif c == "r":
                        print("Blue\n")
                    elif c == "g":
                        print("Green\n")
                    else:
                        print("Red\n")
                elif strike == 1:
                    if c == "b":
                        print("Blue\n")
                    elif c == "r":
                        print("Red\n")
                    elif c == "g":
                        print("Yellow\n")
                    else:
                        print("Green\n")
                else:
                    if c == "b":
                        print("Green\n")
                    elif c == "r":
                        print("Yellow\n")
                    elif c == "g":
                        print("Blue\n")
                    else:
                        print("Red\n")
        finish = input("Is there more? ((y)es or (n)o):\n")
        finish = finish.lower()
        if finish == "n":
            break
    choose()

def memModDisplay(n):
    display = input("\nStage %d: What is the number displayed?:\n" %n)
    valid = 0
    while not valid:
        try:
            int(display)
            if display > 0 and display < 5:
                valid = 1
            else:
                display = input("Error, number must be between 1 and 4:\n")
        except ValueError:
            display = input("Error, number must be an integer between 1 and 4:\n")
    return display

def memModAnswer(choice):
    if choice:
        display = input("What position is the label?:(1-4)\n")
    else:
        display = input("What number is the label @ stated position?:\n")
    valid = 0
    while not valid:
        try:
            int(display)
            if display > 0 and display < 5:
                valid = 1
            else:
                display = input("Error, number must be between 1 and 4:\n")
        except ValueError:
            display = input("Error, number must be an integer between 1 and 4:\n")
    return display

def memoryMod():
    mem = np.array([0,0,0,0,0])
    for x in range(5):
        stage = x+1
        display = memModDisplay(stage)
        if (stage==2 and display==3) or (stage==4 and display==2):  #first position
            print("\nPress button in 1ST position\n")
            button = memModAnswer(0)
            mem[x] = 10+button
        elif stage==1 and (display==1 or display==2):           #second position
            print("\nPress button in 2ND position\n")
            button = memModAnswer(0)
            mem[x] = 20+button
        elif(stage==1 and display==3) or (stage==3 and display==3): #third position
            print("\nPress button in 3RD position\n")
            button = memModAnswer(0)
            mem[x] = 30+button
        elif stage==1 and display==4:                           #fourth position
            print("\nPress button in 4TH position\n")
            button = memModAnswer(0)
            mem[x] = 40+button
        elif(stage==2 and display==1) or (stage==3 and display==4): #label 4
            print("\nPress button LABELED 4\n")
            button = memModAnswer(1)
            mem[x] = (button*10) + 4
        elif(stage==2 and (display==2 or display==4)) or (stage==4 and display==1):  #stage 1 position
            pos = mem[0]/10
            if pos == 1:
                order = "1ST"
            elif pos == 2:
                order = "2ND"
            elif pos == 3:
                order = "3RD"
            else:
                order = "4TH"
            print("\nPress the button in the {} position\n".format(order))
            button = memModAnswer(0)
            mem[x] = (pos*10) + button
        elif(stage==4 and (display==3 or display==4)):  #stage 2 position
            pos = mem[1]/10
            if pos == 1:
                order = "1ST"
            elif pos == 2:
                order = "2ND"
            elif pos == 3:
                order = "3RD"
            else:
                order = "4TH"
            print("\nPress the button in the {} position\n".format(order))
            button = memModAnswer(0)
            mem[x] = (pos*10) + button
        elif(stage==3 and display==2) or (stage==5 and display==1):               #stage 1 label
            pos = mem[0]%10
            print("\nPress the button labeled {}\n".format(pos))
            button = memModAnswer(0)
            mem[x] = button*10 + pos
        elif(stage==3 and display==1) or (stage==5 and display==2):               #stage 2 label
            pos = mem[1]%10
            print("\nPress the button labeled {}\n".format(pos))
            button = memModAnswer(0)
            mem[x] = button*10 + pos
        elif stage==5 and display==4:                                             #stage 3 label
            pos = mem[2]%10
            print("\nPress the button labeled {}\n".format(pos))
        elif stage==5 and display==3:                                             #stage 4 label
            pos = mem[3]%10
            print("\nPress the button labeled {}\n".format(pos))
        else:
            print("Something went wrong, please try again.")
    choose()
    
def module(num):
    if num is 1:
        wireMod()
    elif num is 2:
        buttonMod()
    elif num is 3:
        simonMod()
    elif num is 4:
        memoryMod()
    elif num is 0:
        print("\nComplete")
        return
        
def choose():
    choice = input("\nPlease enter module selection:\n1)\tWires\n2)\tButton\n3)\tSimon Says\n4)\tMemory\n0)\tExit\n")
    choice = int(choice)
    module(choice)

serial = input("Enter the serial number:\n")
serialValid()
battery = input("Enter number of batteries:\n")
batteryValid()
ind= input("Please enter all LIT indicators:\n")
indicators = ind.split()
indicatorValid()
choose()
