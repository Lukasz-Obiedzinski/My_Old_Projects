# program analizujacy sylwetki kobiet dla Pauli
# features:
# obrazy, test dzialania, opis sylwetki

from appJar import gui

def check1(ch):
    if ch=="Zatwierdz":
        ramiona = str(win.getOptionBox("Ramiona wzgledem bioder sa:"))
        char=str(win.getOptionBox("Char:"))
        biust = str(win.getOptionBox("Biust"))
        talia = str(win.getOptionBox("Talia"))
        nogi = str(win.getOptionBox("Nogi"))


        if char=="Ramiona":
            if ramiona=="Szersze":
                if biust=="Duzy":
                    if talia=="Niewidoczna":
                        if nogi=="Szczuple":
                            print ("kielich")
                            win.infoBox("Twoja sylwetka to: ", win.addImage("kielich","typkielich.gif"))
                    elif talia=="Zarysowana":
                        if nogi=="Szczuple":
                            print ("Wazon")
                elif biust=="W sam raz":
                    if talia =="Wcieta":
                        if nogi=="Masywne":
                            print("klepsydra")
                    elif talia == "Niewidoczna":
                        if nogi=="Szczuple":
                            print ("Rozek")
        elif char=="Zadna":
            if ramiona =="Takie same":
                if biust=="Maly" or biust=="W sam raz":
                    if talia=="Niewidoczna":
                        if nogi=="Szczuple":
                            print ("Cegla")
        elif char=="Talia":
            if ramiona =="Takie same":
                if biust =="Maly" or biust=="W sam raz":
                    if talia == "Wcieta":
                        if nogi=="Szczuple":
                            print("Kolumna")
            elif ramiona=="Szersze":
                if biust == "Duzy":
                    if talia=="Wcieta":
                        if nogi=="Masywne Uda":
                            print ("Klepsydra")
        elif char=="Biodra" or char=="Uda":
            if ramiona =="Wezsze":
                if biust == "Maly" or biust == "W sam raz":
                    if talia == "Niewidoczna":
                        if nogi=="Masywne":
                            print ("Gruszka")
        elif char=="Ramiona" or char=="Biodra" or char=="Uda" or char=="Talia":
            if ramiona =="Takie same":
                if biust=="Maly" or biust =="W sam raz":
                    if talia == "Wcieta":
                        if nogi == "Szczuple":
                            print("Kolumna")
        elif char =="Brzuch" or char=="Nogi":
            if ramiona == "Wezsze" or char=="Takie same":
                if biust =="Duzy" or biust == "W sam raz":
                    if talia == "Niewidoczna":
                        if nogi == "Szczuple":
                            print("Lizak")



    elif ch=="Wyjdz":
        win.stop()
    elif ch=="Muzyka":
        win.stopSound()
        win.disableButton("Muzyka")



win = gui("Sylwetka")
win.setGeom("400x300")
win.setResizable(True)
win.loopSound("loop.wav")

# win2=gui("Twoja sylwetka to:")
# win2.setGeom("400x400")
# win2.setResizable(True)


win.addLabel("lb1","Charakterystyczna czesc ciala")
win.addLabelOptionBox("Char:",["Zadna","Biodra","Uda",
                    "Ramiona","Brzuch","Biust","Talia"])
# win.addLabel("lb2","Ramiona wzgledem bioder sa :")
win.addLabelOptionBox("Ramiona wzgledem bioder sa:", ["Szersze","Wezsze","Takie same"])
win.addLabelOptionBox("Biust", ["Duzy","Maly","W sam raz"])
win.addLabelOptionBox("Talia",["Niewidoczna","Zarysowana","Wcieta"])
win.addLabelOptionBox("Nogi",["Masywne uda","Szczuple","Masywne lydki"])


win.addButtons(["Zatwierdz","Wyjdz","Muzyka"],check1)

win.go()