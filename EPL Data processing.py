from tkinter import *
import csv
import numpy as np
import matplotlib.pylab as plt

def main(teamName1, teamName2):
    print(teamName1, " + ", teamName2)

def teams2(teamName1):
    window = Tk()
    window.title("Premier League Data")
    window.geometry("300x400")
    window.configure(background = "black")
    lab = Label(window, text = "Choose First Team", fg = "white", bg = "black")
    butSwan =  Button(window, text = "Swansea", bg = "white", command = lambda: main(teamName1,"SWANSEA"))
    butBurn =  Button(window, text = "Burnley", bg = "white", command = lambda: main(teamName1,"BURNLEY"))
    butNewc =  Button(window, text = "Newcastle", bg = "white", command = lambda: main(teamName1,"NEWCASTLE"))
    butBrom =  Button(window, text = "West Brom", bg = "white", command = lambda: main(teamName1,"WEST BROM"))
    butWat =  Button(window, text = "Watford", bg = "white", command = lambda: main(teamName1,"WATFORD"))
    butBrig =  Button(window, text = "Brighton", bg = "white", command = lambda: main(teamName1,"BRIGHTON"))
    butSund =  Button(window, text = "Sunderland", bg = "white", command = lambda: main(teamName1,"SUNDERLAND"))
    butVilla =  Button(window, text = "Aston Villa", bg = "white", command = lambda: main(teamName1,"ASTON VILLA"))
    butCard =  Button(window, text = "Cardiff", bg = "white", command = lambda: main(teamName1,"CARDIFF"))
    butHudd =  Button(window, text = "Huddersfield", bg = "white", command = lambda: main(teamName1,"HUDDERSFIELD"))
    butHull =  Button(window, text = "Hull City", bg = "white", command = lambda: main(teamName1,"HULL CITY"))
    butFul =  Button(window, text = "Fulham", bg = "white", command = lambda: main(teamName1,"FULHAM"))
    butQpr =  Button(window, text = "QPR", bg = "white", command = lambda: main(teamName1,"QPR"))

    lab.pack()
    butSwan.pack()
    butBurn.pack()
    butNewc.pack()
    butBrom.pack()
    butWat.pack()
    butBrig.pack()
    butSund.pack()
    butVilla.pack()
    butCard.pack()
    butHudd.pack()
    butHull.pack()
    butFul.pack()
    butQpr.pack()

    window.mainloop()
    window.destroy()

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
    butCry =  Button(window, text = "Crystal Palace", bg = "white", command = lambda: teams2("CRYSTAL PALACE"))

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
    butCry.pack()

    window.mainloop()
    window.destroy()

teams1()



