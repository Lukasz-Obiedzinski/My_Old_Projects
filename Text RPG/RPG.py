# programRPG
# Ma możliwość wyboru swojej klasy, imie oraz swoje cechy charakterystyczne
# Ma mieć możliwość wyboru randomowego imienia i nazwiska
# lekki scenariusz RPG na trybie solo
import time
from appJar import gui
from random import *


okno=gui("E R P E G E")
okno.setResizable(False)
okno.setGeom("350x350")



#######################################

# first screen with logo


okno1=gui("E R P E G E")
okno1.setResizable(False)
okno1.setGeom("350x350")



okno1.addLabel("logo","E R P E G E")


def dalej(btn):
        if btn == "Continue":
                okno1.stop()
        else:
                return "nic"


okno1.addButton("Continue",dalej)

okno1.go()


########################################
#Wybor rasy

def btn(btn):
        if btn=="Czlowiek":
                print("JESTES CZLOWIEKIEM")
        elif btn=="Elf":
                print("JESTES ELFEM")
        elif btn=="Krasnolud":
                print("JESTES KRASNOLUDEM")
        elif btn=="Niziolek":
                print("JESTES NIZIOLKIEM")

okno.addLabel("lb1","Wybierz rase")
okno.addButtons(["Czlowiek","Elf","Krasnolud","Niziolek"],btn)


okno.setRelief("GROOVE")




#######################################

# modul losujacy
# Wybor imienia

imiona_ludzi=["Adam","Krystold","Gertrud"]
imiona_ludzi= random(imiona_ludzi)
print (imiona_ludzi)

random
#######################################





#######################################



okno.go()
