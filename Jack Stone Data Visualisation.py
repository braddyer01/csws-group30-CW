#imports all required libraries in the code
from tkinter import *
import csv
import numpy as np
import matplotlib.pylab as plt

#function called for displaying the data to the user
def main(teamName1, teamName2, statChoice):

#declaring all required variables used in the code
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

#opening the csv file for the user
    with open ("english premier league data.csv") as csv_file:
        csvReader = csv.reader(csv_file, delimiter = ",")
        #resetting value of lineCount 
        lineCount = 0

        #code for processing and displaying the data for shots to the user
        if statChoice == "SHOTS":
            for row in csvReader:
                #skipping the first line of the file as it is unused
                if lineCount == 0:
                    lineCount += 1
                #adding all the data into an array
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

            #calculating average for the data
            for i in range(len(shot1)):
                totalShot1 = totalShot1 + float(shot1[i])
            for i in range(len(shot2)):
                totalShot2 = totalShot2 + float(shot2[i])
            avg = totalShot1 / len(shot1)
            avg2 = totalShot2 / len(shot2)
            avg = round(avg, 2)
            avg2 = round(avg2, 2)

            #displaying text based version of the data
            print (teamName1, "averaged", avg, "shots per game")
            print (teamName2, "averaged", avg2, "shots per game")

            #visualising the data for the user
            objects1 = (teamName1, teamName2)
            y_pos = np.arange(len(objects1))
            objects2 = [avg, avg2]

            plt.bar(y_pos, objects2, align="center", alpha =0.5)
            plt.xticks(y_pos,objects1)
            plt.ylabel("AVG Shots")
            plt.title("Teams Average Shots per game")

            plt.show()

        #code for processing and displaying the data for shots on target to the user
        elif statChoice == "SHOTS ON TARGET":
            for row in csvReader:
                #skipping the first line of the file as it is unused
                if lineCount == 0:
                    lineCount += 1
                #adding all the data into an array
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

            #calculating average for the data
            for i in range(len(SOT1)):
                totalSOT1 = totalSOT1 + float(SOT1[i])
            for i in range(len(SOT2)):
                totalSOT2 = totalSOT2 + float(SOT2[i])
            avg = totalSOT1 / len(SOT1)
            avg2 = totalSOT2 / len(SOT2)
            avg = round(avg, 2)
            avg2 = round(avg2, 2)
            
            #displaying text based version of the data
            print (teamName1, "averaged", avg, "shots on target per game")
            print (teamName2, "averaged", avg2, "shots on target per game")

            #visualising the data for the user
            objects1 = (teamName1, teamName2)
            y_pos = np.arange(len(objects1))
            objects2 = [avg, avg2]

            plt.bar(y_pos, objects2, align="center", alpha =0.5)
            plt.xticks(y_pos,objects1)
            plt.ylabel("AVG Shots on Target")
            plt.title("Teams Average Shots on Target")

            plt.show()

        #code for processing and displaying the data for possession to the user
        elif statChoice == "POSSESSION":
            for row in csvReader:
                #skipping the first line of the file as it is unused
                if lineCount == 0:
                    lineCount += 1
                #adding all the data into an array
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

            #calculating average for the data
            for i in range(len(Poss1)):
                totalPoss1 = totalPoss1 + float(Poss1[i])
            for i in range(len(Poss2)):
                totalPoss2 = totalPoss2 + float(Poss2[i])
            avg = totalPoss1 / len(Poss1)
            avg2 = totalPoss2 / len(Poss2)
            avg = round(avg, 2)
            avg2 = round(avg2, 2)

            #displaying text based version of the data
            print (teamName1, "averaged", avg, "% posession")
            print (teamName2, "averaged", avg2, "% possession")

            #visualising the data for the user
            objects1 = (teamName1, teamName2)
            y_pos = np.arange(len(objects1))
            objects2 = [avg, avg2]

            plt.bar(y_pos, objects2, align="center", alpha =0.5)
            plt.xticks(y_pos,objects1)
            plt.ylabel("AVG Possession")
            plt.title("Teams Average Possession per game")

            plt.show()

        #code for processing and displaying the data for fouls to the user
        elif statChoice == "FOULS":
            for row in csvReader:
                #skipping the first line of the file as it is unused
                if lineCount == 0:
                    lineCount += 1
                #adding all the data into an array
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

            #calculating average for the data
            for i in range(len(Fouls1)):
                totalFouls1 = totalFouls1 + float(Fouls1[i])
            for i in range(len(Fouls2)):
                totalFouls2 = totalFouls2 + float(Fouls2[i])
            avg = totalFouls1 / len(Fouls1)
            avg2 = totalFouls2 / len(Fouls2)
            avg = round(avg, 2)
            avg2 = round(avg2, 2)

            #displaying text based version of the data
            print (teamName1, "averaged", avg, "fouls per game")
            print (teamName2, "averaged", avg2, "fouls per game")

            #visualising the data for the user
            objects1 = (teamName1, teamName2)
            y_pos = np.arange(len(objects1))
            objects2 = [avg, avg2]
            
            plt.bar(y_pos, objects2, align="center", alpha =0.5)
            plt.xticks(y_pos,objects1)
            plt.ylabel("AVG Fouls")
            plt.title("Teams Average fouls per game")

            plt.show()
                    

#function for creating the buttons and window for the choice of stats
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


#function for creating the buttons and window the choice of lower ranked teams
def teams2(teamName1):
    window = Tk()
    window.title("Premier League Data")
    window.geometry("300x400")
    window.configure(background = "black")
    lab = Label(window, text = "BOTTOM 13 TEAMS", fg = "white", bg = "black")
    butSwan = Button(window, text = "(15) Swansea", bg = "white", command = lambda: choice(teamName1,"SWANSEA"))
    butBurn = Button(window, text = "(16) Burnley", bg = "white", command = lambda: choice(teamName1,"BURNLEY"))
    butNewc = Button(window, text = "(17) Newcastle", bg = "white", command = lambda: choice(teamName1,"NEWCASTLE"))
    butBrom = Button(window, text = "(18) West Brom", bg = "white", command = lambda: choice(teamName1,"WEST BROM"))
    butWat = Button(window, text = "(19) Watford", bg = "white", command = lambda: choice(teamName1,"WATFORD"))
    butBrig = Button(window, text = "(20) Brighton", bg = "white", command = lambda: choice(teamName1,"BRIGHTON"))
    butSund = Button(window, text = "(21) Sunderland", bg = "white", command = lambda: choice(teamName1,"SUNDERLAND"))
    butVilla = Button(window, text = "(22) Aston Villa", bg = "white", command = lambda: choice(teamName1,"ASTON VILLA"))
    butCard = Button(window, text = "(23) Cardiff", bg = "white", command = lambda: choice(teamName1,"CARDIFF"))
    butHudd = Button(window, text = "(24) Huddersfield", bg = "white", command = lambda: choice(teamName1,"HUDDERSFIELD"))
    butHull = Button(window, text = "(25) Hull City", bg = "white", command = lambda: choice(teamName1,"HULL CITY"))
    butFul = Button(window, text = "(26) Fulham", bg = "white", command = lambda: choice(teamName1,"FULHAM"))
    butQpr = Button(window, text = "(27) QPR", bg = "white", command = lambda: choice(teamName1,"QPR"))

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

#function for creating button and windows for the choice of higher ranked teams
def teams1():
    window = Tk()
    window.title("Premier League Data")
    window.geometry("300x400")
    window.configure(background = "black")
    lab = Label(window, text = "TOP 14 TEAMS", fg = "white", bg = "black")
    butManC = Button(window, text = "(1) Manchester City", bg = "white", command = lambda: teams2("MAN CITY"))
    butTott = Button(window, text = "(2) Tottenham", bg = "white", command = lambda: teams2("TOTTENHAM"))
    butChels = Button(window, text = "(3) Chelsea", bg = "white", command = lambda: teams2("CHELSEA"))
    butLiv = Button(window, text = "(4) Liverpool", bg = "white", command = lambda: teams2("LIVERPOOL"))
    butManU = Button(window, text = "(5) Manchester United", bg = "white", command = lambda: teams2("MAN UTD"))
    butArse = Button(window, text = "(6) Arsenal", bg = "white", command = lambda: teams2("ARSENAL"))
    butWolv = Button(window, text = "(7) Wolves", bg = "white", command = lambda: teams2("WOLVES"))
    butLeic =  Button(window, text = "(8) Leicester", bg = "white", command = lambda: teams2("LEICESTER CITY"))
    butSheff = Button(window, text = "(9) Sheffield United", bg = "white", command = lambda: teams2("SHEFFIELD UNITED"))
    butEver = Button(window, text = "(10) Everton", bg = "white", command = lambda: teams2("EVERTON"))
    butSout = Button(window, text = "(11) Southampton", bg = "white", command = lambda: teams2("SOUTHAMPTON"))
    butWest = Button(window, text = "(12) West Ham", bg = "white", command = lambda: teams2("WEST HAM"))
    butStoke = Button(window, text = "(13) Stoke City", bg = "white", command = lambda: teams2("STOKE"))
    butCry = Button(window, text = "(14) Crystal Palace", bg = "white", command = lambda: teams2("CRYSTAL PALACE"))

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



