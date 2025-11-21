import os
#█

def cls():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def bootupscreen():
    print("████████████████████████████")
    print("████welcome to py OS████████")
    print("████████████████████████████")
    print("████████████████████████████")
    print("████████████████████████████")
bootupscreen()
screen1 = 1



def screen():
    if screen1 == 1:
        
        
        print("███████████████")
        print("███████████████")
        print("███████████████")
        print("███████████████")
        print("menu███████████")
        print("type ''m'' or \n''menu'' to enter the menu")
    else:
        menu()

def menu():
    if screen1 == 2:
        
        
        print("███████████████")
        print("type ''m'' or \n''menu'' to exit the menu")
        print("calculator")
        print("guess the number")
        print("add notes")
        print("load notes")
        print("clear")
        print("███████████████")
    else:
        screen()
    


def calc():
    cls()
    print("enter any equasion")
    calcinput1 = input()
    calcoutput1 = eval(calcinput1)
    print(calcoutput1)

def gtn():
    print("i chose a random number from 1 to 10")
    import random
    randomnumbertoguess = random.randint(1, 10)
    gtnguess = 0
    keepgoing = 1
    while keepgoing == 1:
        gtnguess = input()
        if int(gtnguess) < randomnumbertoguess:
            print("thats too low")
        if int(gtnguess) > randomnumbertoguess:
            print("thats too high")
        if int(gtnguess) == randomnumbertoguess:
            print("you guessed it!")
            keepgoing = 0
note = ""
def anotes():
    global note
    note = input("your notepad\n")

def lnotes():
    print(note)


screen()


while True:
    screen()

    screeninput = input("$> ")
    if screen1 == 1:
        if screeninput == "m" or "menu" == 1:
            screen1 = 2
    elif screen1 == 2:
        if screeninput == "m" or "menu" and screen1 == 2:
            screen1 = 1
        if screeninput == "calculator":
            calc()
        if screeninput == "guess the number":
            gtn()
        if screeninput == "add notes":
            anotes()
        if screeninput == "load notes":
            lnotes()
    elif screeninput == "cls" or "clear":
        cls()
