from tkinter import *
import csv
import numpy as np
import matplotlib.pylab as plt

def main(teamName1, teamName2, statChoice):

    shot1 = []
    shot2 = []
    SOT1 = []
    SOT2 = []
    Poss1 = []
    Poss2 = []
    Fouls1 = []
    Fouls2 = []
    totalShot1 = 0
    totalShot2 = 0
    totalPoss1 = 0
    totalPoss2 = 0
    totalSOT1 = 0
    totalSOT2 = 0
    totalFouls1 = 0
    totalFouls2 = 0

    with open ("english premier league data.csv") as csv_file:
        csvReader = csv.reader(csv_file, delimiter = ",")
        lineCount = 0
        if statChoice == "SHOTS":
            for row in csvReader:
                if lineCount == 0:
                    lineCount += 1
                else:
                    while (row[1] == teamName1 or row[2] == teamName1):
                        if row[1] == teamName1:
                            shot1.append(row[12])
                            break
                        else:
                            shot1.append(row[25])
                            break
                    while (row[1] == teamName2 or row[2] == teamName2):
                        if row[1] == teamName2:
                            shot2.append(row[12])
                            break
                        else:
                            shot2.append(row[25])
                            break
            lineCount += 1

            for i in range(len(shot1)):
                totalShot1 = totalShot1 + float(shot1[i])
            for i in range(len(shot2)):
                totalShot2 = totalShot2 + float(shot2[i])
            avg = totalShot1 / len(shot1)
            avg2 = totalShot2 / len(shot2)
            avg = round(avg, 2)
            avg2 = round(avg2, 2)
            print (teamName1, "averaged", avg, "shots per game")
            print (teamName2, "averaged", avg2, "shots per game")

            objects1 = (teamName1, teamName2)
            y_pos = np.arange(len(objects1))
            objects2 = [avg, avg2]

            plt.bar(y_pos, objects2, align="center", alpha =0.5)
            plt.xticks(y_pos,objects1)
            plt.ylabel("AVG Shots")
            plt.title("Teams Average Shots per game")

            plt.show()

        elif statChoice == "SHOTS ON TARGET":
            for row in csvReader:
                if lineCount == 0:
                    lineCount += 1
                else:
                    while (row[1] == teamName1 or row[2] == teamName1):
                        if row[1] == teamName1:
                            SOT1.append(row[11])
                            break
                        else:
                            SOT1.append(row[25])
                            break
                    while (row[1] == teamName2 or row[2] == teamName2):
                        if row[1] == teamName2:
                            SOT2.append(row[11])
                            break
                        else:
                            SOT2.append(row[24])
                            break
            lineCount += 1

            for i in range(len(SOT1)):
                totalSOT1 = totalSOT1 + float(SOT1[i])
            for i in range(len(SOT2)):
                totalSOT2 = totalSOT2 + float(SOT2[i])
            avg = totalSOT1 / len(SOT1)
            avg2 = totalSOT2 / len(SOT2)
            avg = round(avg, 2)
            avg2 = round(avg2, 2)
            print (teamName1, "averaged", avg, "shots on target per game")
            print (teamName2, "averaged", avg2, "shots on target per game")

            objects1 = (teamName1, teamName2)
            y_pos = np.arange(len(objects1))
            objects2 = [avg, avg2]

            plt.bar(y_pos, objects2, align="center", alpha =0.5)
            plt.xticks(y_pos,objects1)
            plt.ylabel("AVG Shots on Target")
            plt.title("Teams Average Shots on Target")

            plt.show()

        elif statChoice == "POSSESSION":
            for row in csvReader:
                if lineCount == 0:
                    lineCount += 1
                else:
                    while (row[1] == teamName1 or row[2] == teamName1):
                        if row[1] == teamName1:
                            Poss1.append(row[8])
                            break
                        else:
                            Poss1.append(row[9])
                            break
                    while (row[1] == teamName2 or row[2] == teamName2):
                        if row[1] == teamName2:
                            Poss2.append(row[8])
                            break
                        else:
                            Poss2.append(row[9])
                            break
            lineCount += 1

            for i in range(len(Poss1)):
                totalPoss1 = totalPoss1 + float(Poss1[i])
            for i in range(len(Poss2)):
                totalPoss2 = totalPoss2 + float(Poss2[i])
            avg = totalPoss1 / len(Poss1)
            avg2 = totalPoss2 / len(Poss2)
            avg = round(avg, 2)
            avg2 = round(avg2, 2)
            print (teamName1, "averaged", avg, "% posession")
            print (teamName2, "averaged", avg2, "% possession")

            objects1 = (teamName1, teamName2)
            y_pos = np.arange(len(objects1))
            objects2 = [avg, avg2]

            plt.bar(y_pos, objects2, align="center", alpha =0.5)
            plt.xticks(y_pos,objects1)
            plt.ylabel("AVG Possession")
            plt.title("Teams Average Possession per game")

            plt.show()

        elif statChoice == "FOULS":
            for row in csvReader:
                if lineCount == 0:
                    lineCount += 1
                else:
                    while (row[1] == teamName1 or row[2] == teamName1):
                        if row[1] == teamName1:
                            Fouls1.append(row[19])
                            break
                        else:
                            Fouls1.append(row[32])
                            break
                    while (row[1] == teamName2 or row[2] == teamName2):
                        if row[1] == teamName2:
                            Fouls2.append(row[19])
                            break
                        else:
                            Fouls2.append(row[32])
                            break
            lineCount += 1

            for i in range(len(Fouls1)):
                totalFouls1 = totalFouls1 + float(Fouls1[i])
            for i in range(len(Fouls2)):
                totalFouls2 = totalFouls2 + float(Fouls2[i])
            avg = totalFouls1 / len(Fouls1)
            avg2 = totalPoss2 / len(Fouls2)
            avg = round(avg, 2)
            avg2 = round(avg2, 2)
            print (teamName1, "averaged", avg, "fouls per game")
            print (teamName2, "averaged", avg2, "fouls per game")

            objects1 = (teamName1, teamName2)
            y_pos = np.arange(len(objects1))
            objects2 = [avg, avg2]

            plt.bar(y_pos, objects2, align="center", alpha =0.5)
            plt.xticks(y_pos,objects1)
            plt.ylabel("AVG Fouls")
            plt.title("Teams Average fouls per game")

            plt.show()
                    


def choice(teamName1, teamName2):
    window = Tk()
    window.title("Premier League Data")
    window.geometry("250x250")
    window.configure(background = "black")
    lab = Label(window, text = "Choose visualisation type", fg = "white", bg = "black")
    butShot =  Button(window, text = "Shots", bg = "white", command = lambda: main(teamName1, teamName2, "SHOTS"))
    butSOT =  Button(window, text = "Shots on Target", bg = "white", command = lambda: main(teamName1, teamName2, "SHOTS ON TARGET"))
    butPoss =  Button(window, text = "AVG Posession", bg = "white", command = lambda: main(teamName1, teamName2, "POSSESSION"))
    butFouls = Button(window, text = "AVG Fouls", bg = "white", command = lambda: main(teamName1, teamName2, "FOULS"))

    lab.pack()
    butShot.pack()
    butSOT.pack()
    butPoss.pack()
    butFouls.pack()

    window.mainloop()



def teams2(teamName1):
    window = Tk()
    window.title("Premier League Data")
    window.geometry("300x400")
    window.configure(background = "black")
    lab = Label(window, text = "Choose Second Team", fg = "white", bg = "black")
    butSwan = Button(window, text = "Swansea", bg = "white", command = lambda: choice(teamName1,"SWANSEA"))
    butBurn = Button(window, text = "Burnley", bg = "white", command = lambda: choice(teamName1,"BURNLEY"))
    butNewc = Button(window, text = "Newcastle", bg = "white", command = lambda: choice(teamName1,"NEWCASTLE"))
    butBrom = Button(window, text = "West Brom", bg = "white", command = lambda: choice(teamName1,"WEST BROM"))
    butWat = Button(window, text = "Watford", bg = "white", command = lambda: choice(teamName1,"WATFORD"))
    butBrig = Button(window, text = "Brighton", bg = "white", command = lambda: choice(teamName1,"BRIGHTON"))
    butSund = Button(window, text = "Sunderland", bg = "white", command = lambda: choice(teamName1,"SUNDERLAND"))
    butVilla = Button(window, text = "Aston Villa", bg = "white", command = lambda: choice(teamName1,"ASTON VILLA"))
    butCard = Button(window, text = "Cardiff", bg = "white", command = lambda: choice(teamName1,"CARDIFF"))
    butHudd = Button(window, text = "Huddersfield", bg = "white", command = lambda: choice(teamName1,"HUDDERSFIELD"))
    butHull = Button(window, text = "Hull City", bg = "white", command = lambda: choice(teamName1,"HULL CITY"))
    butFul = Button(window, text = "Fulham", bg = "white", command = lambda: choice(teamName1,"FULHAM"))
    butQpr = Button(window, text = "QPR", bg = "white", command = lambda: choice(teamName1,"QPR"))

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

def teams1():
    window = Tk()
    window.title("Premier League Data")
    window.geometry("300x400")
    window.configure(background = "black")
    lab = Label(window, text = "Choose First Team", fg = "white", bg = "black")
    butManC = Button(window, text = "Manchester City", bg = "white", command = lambda: teams2("MAN CITY"))
    butTott = Button(window, text = "Tottenham", bg = "white", command = lambda: teams2("TOTTENHAM"))
    butChels = Button(window, text = "Chelsea", bg = "white", command = lambda: teams2("CHELSEA"))
    butLiv = Button(window, text = "Liverpool", bg = "white", command = lambda: teams2("LIVERPOOL"))
    butManU = Button(window, text = "Manchester United", bg = "white", command = lambda: teams2("MAN UTD"))
    butArse = Button(window, text = "Arsenal", bg = "white", command = lambda: teams2("ARSENAL"))
    butWolv = Button(window, text = "Wolves", bg = "white", command = lambda: teams2("WOLVES"))
    butLeic =  Button(window, text = "Leicester", bg = "white", command = lambda: teams2("LEICESTER CITY"))
    butSheff = Button(window, text = "Sheffield United", bg = "white", command = lambda: teams2("SHEFFIELD UNITED"))
    butEver = Button(window, text = "Everton", bg = "white", command = lambda: teams2("EVERTON"))
    butSout = Button(window, text = "Southampton", bg = "white", command = lambda: teams2("SOUTHAMPTON"))
    butWest = Button(window, text = "West Ham", bg = "white", command = lambda: teams2("WEST HAM"))
    butStoke = Button(window, text = "Stoke City", bg = "white", command = lambda: teams2("STOKE"))
    butCry = Button(window, text = "Crystal Palace", bg = "white", command = lambda: teams2("CRYSTAL PALACE"))

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



