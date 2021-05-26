import random

random.seed()

list_dice20 = [0]
list_dice6 = [0]

def strenght_function():

    f = open("rpgame.txt", "rt") #öppnar rpgame och läser det i den

    strenght = "Strenght:" #vad den letar efter

    for line in f:

        if strenght in line: #ifall den hittar det den letar efter

            print(line[10:11]) #skriver ut en del av det skrivet i filen bara

    f.close()

def dice20_function():

    print(random.randint(1, 20)) #tärning mellan 1-20

def dice6_function():

    print(random.randint(1, 6)) #tärning mellan 1-6

def startfunction():
    
    typen = input("Say 'dice6, dice20, strenght:")
    error = "error"
    food = ["1"]

    for raw_input in food:
        if typen == "dice20":
            dice20_function()
        elif typen == "dice6":
            dice6_function()
        elif typen == "strenght":
            strenght_function()
        else:
            print(error) #error meddelande
            
startfunction() # startar allt