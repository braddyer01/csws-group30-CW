from tkinter import *
import csv
import numpy as np
import matplotlib.pylab as plt

def teams2():
    print()

def teams1():
    window = Tk()
    window.title("Premier League Data")
    window.geometry("300x400")
    window.configure(background = "black")
    lab = Label(window, text = "Choose First Team", fg = "white", bg = "black")
    butManC =  Button(window, text = "Manchester City", bg = "white", command = lambda: teams2("MAN CITY"))
    butTott =  Button(window, text = "Tottenham", bg = "white", command = lambda: teams2("TOTTENHAM"))
    butChels =  Button(window, text = "Chelsea", bg = "white", command = lambda: teams2("CHELSEA"))
    butLiv =  Button(window, text = "Liverpool", bg = "white", command = lambda: teams2("LIVERPOOL"))
    butManU =  Button(window, text = "Manchester United", bg = "white", command = lambda: teams2("MAN UNITED"))
    butArse =  Button(window, text = "Arsenal", bg = "white", command = lambda: teams2("ARSENAL"))
    butWolv =  Button(window, text = "Wolves", bg = "white", command = lambda: teams2("WOLVES"))
    butLeic =  Button(window, text = "Leicester", bg = "white", command = lambda: teams2("LEICESTER CITY"))
    butSheff =  Button(window, text = "Sheffield United", bg = "white", command = lambda: teams2("SHEFFIELD UNITED"))
    butEver =  Button(window, text = "Everton", bg = "white", command = lambda: teams2("EVERTON"))
    butSout =  Button(window, text = "Southampton", bg = "white", command = lambda: teams2("SOUTHAMPTON"))
    butWest =  Button(window, text = "West Ham", bg = "white", command = lambda: teams2("WEST HAM"))
    butStoke =  Button(window, text = "Stoke City", bg = "white", command = lambda: teams2("STOKE"))

    lab.pack()
    butManC.pack()
    butTott.pack()
    butChels.pack()
    butLiv.pack()
    butManU.pack()
    butArse.pack()
    butWolv.pack()
    butLeic.pack()
    butSheff.pack()
    butEver.pack()
    butSout.pack()
    butWest.pack()
    butStoke.pack()

    window.mainloop()

teams1()