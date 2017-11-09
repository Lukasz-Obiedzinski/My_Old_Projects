#aplikacja pamietnik z data, pdfem,

from appJar import gui


win = gui("Memorycall")
win.setResizable(False)
win.setGeom("450x250")


# data i godzina
import datetime
czas=datetime.datetime.now()


def button(btn):
    if btn=="Zapisz PDF":
        text = str(win.getTextArea("tx1"))

        # tekst
        pamietnik = open("Pamietnik.txt ", "w")
        pamietnik.writelines()
        pamietnik.write(text)
        pamietnik.close()
        print("wcisniety")
    elif btn == "Wyjdz":
        win.stop()

win.addLabel('lb1',str(czas))
win.addTextArea("tx1")
win.addButtons(["Zapisz PDF","Wyjdz"],button)

win.go()
