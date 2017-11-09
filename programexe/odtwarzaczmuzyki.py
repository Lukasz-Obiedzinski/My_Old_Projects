from appJar import gui

win = gui("MusicL")
win.setResizable(False)
win.setGeom("200x200")

def button(btn):
    if btn == "Play":
        win.playSound('beep-01a.wav')

win.addButton("Play", button)

win.go()