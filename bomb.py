import re
import numpy as np
from maze import Graph, get_instr,selectMaze,mazeStart,mazeEnd,maze

from collections import defaultdict, deque

def wire3(colors):
    i = 0
    #Lowercase all and check for red wires
    for wire in colors:
        wire = wire.lower()
        if wire == 'r':
            i = 1
    if i == 0:
        print('second')
    else:
        #If last wire is white
        if colors[2] == 'w':
            print('last')
        else:
            i = 0
            for wire in colors:
                #Count the blues
                if wire.lower() == 'b':
                    i+=1
            if i > 1:
                #Find location of last blue
                result = len(colors) - 1 - colors[::-1].index('b')
                if result == 0:
                    print('first')
                elif result == 1:
                    print('second')
                else:
                    print('last')
            else:
                print("last")

def wire4(colors):
    red=0
    blue=0
    yellow=0
    for wire in colors:
        wire = wire.lower()
        if wire == "r":
            red+=1
        elif wire == "b":
            blue+=1
        elif wire == "y":
            yellow+=1
    #If greater than 1 red, and last digit serial is even
    if red > 1 and int(serial[5])%2 != 0:
        #Find last red
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
    red = 0
    yellow = 0
    i = 0
    for wire in colors:
        wire = wire.lower()
        if wire == "r":
            red+=1
        elif wire == "y":
            yellow+=1
        elif wire == "k":
            i = 1
    #If there a black and last serial digit is odd
    if i==1 and int(serial[5])%2!=0:
        print("fourth")
    elif red == 1 and yellow > 1:
        print("first")
    elif i == 0:
        print("second")
    else:
        print("first")

def wire6(colors):
    yellow=0
    white=0
    i=0
    for wire in colors:
        wire = wire.lower()
        if wire == "w":
            white+=1
        elif wire == "y":
            yellow+=1
        elif wire == "r":
            i=1
    #If no yellow and last serial digit is odd
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
    while re.search('\d+',text):
        text = input("Error, there are digits detected")
        text = text.lower() 
    v = 0
    while v != 1:
        if text == "detonate" or text == "abort" or text == "press" or text == "hold":
            v = 1
        else:
            text = input("Error, input a valid word: (detonate, abort, press, hold)\n")
            text = text.lower()
    frk = 0
    for ind in list(indicators):
        if ind == "frk":
            frk = 1
    if (battery >1 and text == "detonate") or (battery>2 and frk == 1) or (color=="r" and text == "hold"):
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
            battery = int(battery)
            if int(battery) >= 0:
                valid=1
            else:
                battery = input("Error, number must be positive:\n")
        except ValueError:
            battery = input("Error, number must be an integer:\n")

def indicatorValid():
    global indicators
    indList = ["snd","clr","car","ind","frq","sig","nsa","msa","trn","bob","frk"]
    valid = 0
    if len(indicators) == 0:
        valid = 1
    while not valid:
        for led in indicators:
            led = led.lower()
            if len(led) != 3:
                valid = 0
                indicators = input("Error, input valid indicators:\n")
                indicators = indicators.split()
                break
            else:
                valid= 0
                for x in indList:
                    if x == led:
                        valid = 1
                if not valid:
                    indicators = input("Error, input valid indicators:\n")
                    indicators = indicators.split()
                    break

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
    num = int(input("Number of wires?\n"))
    while num > 6 or num < 3:
        num = int(input("Error, number must be between 3 and 6:\n"))
    wires = input("Order of Wires (using the first letter only, except for Black = k, Blue = b):\n")
    wires = wires.split()
    while len(wires) != num:
        wires = input("Error, incorrect number of wires:\n")
        wires = wires.split()
    wirecol = re.compile("[rRwWyYbBkK]")
    v = 0
    #validate colors
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
        strike = int(input("Number of strikes:\n"))
        v = 0
        #Sanitize strike number
        while not v:
            try:
                strike = int(strike)
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
    #validate 1-4 ints
    while not valid:
        try:
            display = int(display)
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
        display = input("What number is the label @ the stated position?:(1-4)\n")
    valid = 0
    #validate label
    while not valid:
        try:
            display = int(display)
            if display > 0 and display < 5:
                valid = 1
            else:
                display = input("Error, number must be between 1 and 4:\n")
        except ValueError:
            display = input("Error, number must be an integer between 1 and 4:\n")
    return display

def memoryMod():
    mem = np.array([0,0,0,0,0])
    #position and lable are stored as tens digit and ones digit respectively
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

def morseMod():
    decode = {'a':'.-','b':'-...','c':'-.-.','e':'.','f':'..-.','h':'....','i':'..','l':'.-..','m':'--',
    'o':'---','r':'.-.','s':'...','t':'-','v':'...-','x':'-..-',}     #only 15 unique letters for all possible answers
    code = input("Please enter the first three letters using '.' and '-', separated by spaces:\n")
    #sanitize morse by checking for letters, digits, or underscore
    delim = re.compile("[a-zA-Z0-9,_=!@#$%^&*]")
    v = re.match(delim,code)
    while v:
        code = input("Error, detected characters that were not '.' or '-' please try again:\n")
        v = re.match(delim,code)
    code = code.split()
    result = ''
    for letter in code:
        try:
            result += list(decode.keys())[list(decode.values()).index(letter)]
        except ValueError:
            print("Error, there was an invalid morse sequence for a letter.")
            morseMod()
    freq = 3.500
    if result == 'she':
        freq = 3.505
    elif result == 'hal':
        freq = 3.515
    elif result == 'sli':
        freq = 3.522
    elif result == 'tri':
        freq = 3.532
    elif result == 'box':
        freq = 3.535
    elif result == 'lea':
        freq = 3.542
    elif result == 'str':
        freq = 3.545
    elif result == 'bis':
        freq = 3.552
    elif result == 'fli':
        freq = 3.555
    elif result == 'bom':
        freq = 3.565
    elif result == 'bre':
        freq = 3.572
    elif result == 'bri':
        freq = 3.575
    elif result == 'ste':
        freq = 3.582
    elif result == 'sti':
        freq = 3.592
    elif result == 'vec':
        freq = 3.595
    elif result == 'bea':
        freq = 3.600
    if freq != 3.500:
        print("\nPlease input frequency {} MHz\n".format(freq))
    else:
        print("Error, that was not a sequence of valid letters, please try again\n")
    choose()

def compwireMod():
    port = input("Is there a parallel port on the bomb? (y/n):\n")
    if port == 'y':
        parallel = 1
    else:
        parallel = 0
    done = 0
    while not done:
        wire = input("Describe your wire using color (red then/or blue), symbol, and light\nExample:\nrb*l = red&blue&star&light\nwhite wires should not be input\nrbl = red&blue&light\nenter 'd' for done):\n")
        #sanitize wire
        wire = wire.lower()
        val = re.compile("[rb*l]")
        v = re.match(val,wire)
        while not v:
            wire = input("Please enter valid characters to describe your wire, valid characters are: (r, b, *, l)\n")
            wire = wire.lower()
            v = re.match(val,wire)
        if wire == 'l' or wire == 'b*' or wire == 'rb*l':
            print("\nDO NOT CUT\n")         #dont cut
        elif wire == 'w' or wire == 'r*' or wire == '*':
            print("\nCUT\n")                #cut
        elif wire == 'r' or wire == 'b' or wire == 'rb' or wire == 'rbl':
            if int(serial[5])%2==0:              #serial
                print("\nCUT\n")
            else:
                print("\nDO NOT CUT\n")
        elif wire == 'rl' or wire == 'rb*' or wire == 'b*l':
            if parallel:                    #parallel
                print("\nCUT\n")
            else:
                print("\nDO NOT CUT\n")
        elif wire == 'rl' or wire == 'r*l' or wire == '*l':
            if battery >= 2:
                print("\nCUT\n")
            else:
                print("\nDO NOT CUT\n")
        elif wire == 'd':
            done = 1
    choose()

def wiresequenceMod():
    red = 0
    black = 0
    blue = 0
    done = 0
    while not done:
        wire = input("\nPlease enter the color and what letter is connected to it separated by a space: (black = k, done = d)\nExample: \nr a = Red to A\nk c = Black to C\n")
        #wire sanitize
        wire = wire.lower()
        col = re.compile("[kbrd]")
        alph = re.compile("[abc]")
        wire = wire.split()
        v = 0
        x = 0
        while not v:
            if x == 0:
                v = re.match(col,wire[x])
            else:
                v = re.match(alph,wire[x])
            if not v:
                wire = input("Error, detected invalid characters, please try again\n")
                wire = wire.lower()
                wire = wire.split() 
                x = 0
            else:
                x+=1
                if x>1:
                    break
                v = 0
        if wire[0] == 'd':
            done = 1
            break
        if wire[0] == 'r':
            red+=1
            color = 0
        elif wire[0] == 'b':
            blue+=1
            color = 1
        elif wire[0] == 'k':
            black+=1
            color = 2
        letter = wire[1]
        if color == 0:          #red
            if (red == 3 or red == 4 or red == 6 or red == 7 or red==8) and letter == 'a':
                print("\nCUT\n")
            elif (red == 2 or red == 5 or red == 7 or red == 8 or red == 0) and letter == 'b':
                print("\nCUT\n")
            elif (red == 1 or red == 4 or red == 6 or red == 7) and letter == 'c':
                print("\nCUT\n")
            else:
                print("\nSKIP\n")
        elif color == 1:        #blue
            if (blue == 2 or blue == 4 or blue == 8 or blue == 9) and letter == 'a':
                print("\nCUT\n")
            elif (blue == 1 or blue == 3 or blue == 5 or blue == 6) and letter == 'b':
                print("\nCUT\n")
            elif (blue == 2 or blue == 6 or blue == 8) and letter == 'c':
                print("\nCUT\n")
            else:
                print("\nSKIP\n")
        else:                   #black
            if (black == 1 or black == 2 or black == 4 or black == 7) and letter == 'a':
                print("\nCUT\n")
            elif (black == 1 or black == 3 or black == 5 or black == 6 or black == 7) and letter == 'b':
                print("\nCUT\n")
            elif (black == 1 or black == 2 or black == 4 or black == 6 or black == 8 or black == 9) and letter == 'c':
                print("\nCUT\n")
            else:
                print("\nSKIP\n")
    choose()

def whosonMod():
    displayDict = {'yes': 3,'first': 2,'display': 6,'okay': 2,'says': 6,
    'nothing': 3, ' ': 5,'blank': 4,'no': 6,'led': 3,
    'lead': 6,'read': 4,'red': 4,'reed': 5,'leed': 5,
    'hold on': 6,'you': 4,'you are': 6,'your': 4,"you're": 4,
    'ur': 1,'there': 6,"they're": 5,'their': 4,'they are': 3,
    'see': 6,'c': 2,'cee': 6}
    tableDict = {'ready': ["yes","okay","what","middle","left","press","right","blank","ready","no","first","uhhh","nothing","wait"],
    'first': ["left","okay","yes","middle","no","right","nothing","uhhh","wait","ready","blank","what","press","first"],
    'no': ["blank","uhhh","wait","first","what","ready","right","yes","nothing","left","press","okay","no","middle"],
    'blank': ["wait","right","okay","middle","blank","press","ready","nothing","no","what","left","uhhh","yes","first"],
    'nothing': ["uhhh","right","okay","middle","yes","blank","no","press","left","what","wait","first","nothing","ready"],
    'yes': ["okay","right","uhhh","middle","first","what","press","ready","nothing","yes","left","blank","no","wait"],
    'what': ["uhhh","what","left","nothing","ready","blank","middle","no","okay","first","wait","yes","press","right"],
    'uhhh': ["ready","nothing","left","what","okay","yes","ight","no","press","blank","uhhh","middle","wait","first"],
    'left': ["right","left","first","no","middle","yes","blank","what","uhhh","wait","press","ready","okay","nothing"],
    'right': ["yes","nothing","ready","press","no","wait","what","right","middle","left","uhhh","blank","okay","first"],
    'middle': ["blank","ready","okay","what","nothing","press","no","wait","left","middle","right","first","uhhh","yes"],
    'okay': ["middle","no","first","yes","uhhh","nothing","wait","okay","left","ready","blank","press","what""right"],
    'wait': ["uhhh","no","blank","okay","yes","left","first","press","what","wait","nothing","ready","right","middle"],
    'press': ["right","middle","yes","ready","press","okay","nothing","uhhh","blank","left","first","what","no","wait"],
    'you': ["sure","you are","your","you're","next","uh huh","ur","hold","what?","hold","like","done"],
    'you are': ["your","next","like","uh huh","what?","done","uh uh","hold","you","u","you're","sure","ur","you are"],
    'your': ["uh uh","you are","uh huh","your","next","ur","sure","u","you're","you","what?","hold","like","done"],
    "you're": ["you","you're","ur","next","uh uh","you are","u","your","what?","uh huh","sure","done","like","hold"],
    'ur': ["done","u","ur","uh huh","what?","sure","your","hold","you're","like","next","uh uh","you are","you"],
    'u':["uh huh","sure","next","what?","you're","ur","uh uh","done","u","you","like","hold","you are","your"],
    'uh huh':["uh huh","your","you are","you","done","hold","uh uh","next","sure","like","you're","ur","u","what?"],
    'uh uh':["ur","u","you are","you're","next","uh uh","done""you","uh huh","like","your","sure","hold","what?"],
    'what?':["you","hold","you're","your","u","done","uh uh","like","you are","uh huh","ur","next","what?","sure"],
    'done':["sure","uh huh","next","what?","your","ur","you're","hold","like","you","u","you are","uh uh","done"],
    'next':["what?","uh huh","uh uh","your","hold","sure","next","like","done","you are","ur","you're","u","you"],
    'hold':["you are","u","done","uh uh","you","ur","sure","what?","you're","next","hold","uh huh","your","like"],
    'sure':["you are","done","like","you're","you","hold","uh huh","ur","sure","u","what?","next","your","uh uh"],
    'like':["you're","next","u","ur","hold","done","uh uh","what?","uh huh","you","like","sure","you are","your"]}
    done = 0
    while not done:
        display = input("\nPlease input word on display, please enter ' ' for a blank display:\n")
        #Sanitize display
        if display == 'd':
            break
        label = list(displayDict.values())[list(displayDict.keys()).index(display)]
        if label == 1:
            position = input("\nPlease input word on label in the TOP LEFT:\n")
        elif label == 2:
            position = input("\nPlease input word on label in the TOP RIGHT:\n")
        elif label == 3:
            position = input("\nPlease input word on label in the MIDDLE LEFT:\n")
        elif label == 4:
            position = input("\nPlease input word on label in the MIDDLE RIGHT:\n")
        elif label == 5:
            position = input("\nPlease input word on label in the BOTTOM LEFT:\n")
        else:
            position = input("\nPlease input word on label in the BOTTOM RIGHT:\n")
        #sanitize position
        table = tableDict[position]
        print("\nPlease press the first word in this list:")
        print(', '.join(table))
        print("\n")
    choose()

def mazeMod():
    maze()
    choose()

def passMod():
    tableList = ["about","after","again","below","could","every","first","found","great","house",
    "large","learn","never","other","place","plant""point","right","small","sound","spell","still","study","their","there",
    "these","thing","think","three","water","where","which","world","would","write"]
    num = re.compile("[0-9]")
    first = input("\nPlease enter the 6 letters available in the first column:\n")
    v = 0
    first = first.lower()
    first = first.split()
    x = 0
    while not v:
        v = re.match(num, first[x])
        if v:
            print("{}".format(first[x]))
            first = input("Error, detected invalid characters, please try again\n")
            first = first.lower()
            first = first.split() 
            x = 0
        else:
            x+=1
            if x>5:
                break
        v = 0
    second = input("\nPlease enter the 6 letters available in the second column:\n")
    v = 0
    second = second.lower()
    second = second.split()
    x = 0
    while not v:
        v = re.match(num, second[x])
        if v:
            second = input("Error, detected invalid characters, please try again\n")
            second = second.lower()
            second = second.split() 
            x = 0
        else:
            x+=1
            if x>5:
                break
        v = 0
    third = input("\nPlease enter the 6 letters available in the third column:\n")
    v = 0
    third = third.lower()
    third = third.split()
    x = 0
    while not v:
        v = re.match(num,third[x])
        if v:
            third = input("Error, detected invalid characters, please try again\n")
            third = third.lower()
            third = third.split() 
            x = 0
        else:
            x+=1
            if x>5:
                break
        v = 0
    for a in first:
        for b in second:
            for c in third:
                attempt = a+b+c
                for word in tableList:
                    if word.find(attempt)==0:
                        print("\nTry the word:\n {}".format(word))
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
    elif num is 5:
        morseMod()
    elif num is 6:
        compwireMod()
    elif num is 7:
        wiresequenceMod()
    elif num is 8:
        mazeMod()
    elif num is 9:
        passMod()
    elif num is 10:
        whosonMod()
    elif num is 0:
        print("\nComplete")
        return
            
def choose():
    choice = input("\nPlease enter module selection:\n1)\tWires\n2)\tButton\n3)\tSimon Says\n4)\tMemory\n5)\tMorse\n6)\tComplicated Wires\n7)\tWire Sequences\n8)\tMaze\n9)\tPassword\n10)\tWhose on First\n0)\tExit\n")
    choice = int(choice)
    module(choice)

serial = input("Enter the serial number:  (Case insensitive)\n")
serialValid()
battery = input("Enter number of batteries:\n")
batteryValid()
ind= input("Please enter all LIT indicators:\n")
indicators = ind.split()
indicatorValid()
choose()
