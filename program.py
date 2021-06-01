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

def smidighet_function():

    f = open("stats.txt", "rt") #öppnar rpgame och läser det i den

    smidighet = "Smidighet:" #vad den letar efter

    for line in f:

        if smidighet in line: #ifall den hittar det den letar efter

            print(line[11:13]) #skriver ut en del av det skrivet i filen bara

    f.close()

def smidighetcheck_function():
    
    färdigheter = input("Type Smidighet if you want the value:") #frågar vad vi vill veta

    error = "Not right value given." #error som vissas ifall fel värde är inskriven

    food = ["1"]

    for raw_input in food:
        if färdigheter == "Smidighet":
            smidighet_function()
        else:
            print(error)


def dice20_function():

    print(random.randint(1, 20)) #tärning mellan 1-20

def dice6_function():

    print(random.randint(1, 6)) #tärning mellan 1-6

def startfunction():
    
    typen = input("Say 'dice6, dice20, strenght, smidighet:")
    error = "Not right value given."
    food = ["1"]

    for raw_input in food:
        if typen == "dice20":
            dice20_function()
        elif typen == "dice6":
            dice6_function()
        elif typen == "strenght":
            strenght_function()
        elif typen == "smidighet":
            smidighetcheck_function()
        else:
            print(error) #error meddelande
            
startfunction() # startar allt
