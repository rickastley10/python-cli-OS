
#█

def stop():
    exit()

def bootupscreen():
    print("████████████████████████████")
    print("████welcome to py OS████████")
    print("████████████████████████████")
    print("████████████████████████████")
    print("████████████████████████████")
bootupscreen()
screen1 = 2



def menu():
    if screen1 == 2:
        
        
        print("███████████████")
        print("1.calculator")
        print("2.guess the number")
        print("3.add notes")
        print("4.load notes")
        print("5.shutdown")
        print("███████████████")

    


def a1():

    print("enter any equasion")
    calcinput1 = input()
    calcoutput1 = eval(calcinput1)
    print(calcoutput1)

def a2():
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
def a3():
    global note
    note = input("your notepad\n")

def a4():
    print(note)





while True:
    menu()

    screeninput = input("$> ")

    if screen1 == 2:

        if screeninput == "calculator" or screeninput =="1":
            a1()
        if screeninput == "guess the number"or screeninput =="2":
            a2()
        if screeninput == "add notes"or screeninput =="3":
            a3()
        if screeninput == "load notes"or screeninput =="4":
            a4()
        if screeninput == "shutdown" or screeninput =="5":
            stop()

