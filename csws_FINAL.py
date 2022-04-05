#imports---------------------------------------------------------------------------------------------------------
from tkinter import *
import csv
from unicodedata import decimal
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
#page one--------------------------------------------------------------------------------------------------------
def page_one():
    key = 0
    exciteArray = []
    
    print ("""-------------------PAGE1-------------------
    1) View Data
    2) Visualisation
    0) EXIT
""")
    while key == 0:
        choice = input("""Please choose a page option: """)
        if choice == "0":
            key = 1
            menu()
        elif choice == "1":
            def main():
                
                window = Tk()
                window.iconbitmap("favicon.ico")
                window.title("EPL Data")
                window.geometry("300x600")
                window.configure(background = "black")
                labl = Label(window, text = "", fg = "white", bg = "black")
                buttManutd = Button(window, text = "MAN UTD", bg = "white", command = lambda: parse_target("MAN UTD"))
                buttSwan = Button(window, text = "SWANSEA", bg = "white", command = lambda: parse_target("SWANSEA"))
                buttBrom = Button(window, text = "WEST BROM", bg = "white", command = lambda: parse_target("WEST BROM"))
                buttSun = Button(window, text = "SUNDERLAND", bg = "white", command = lambda: parse_target("SUNDERLAND"))
                buttLeic = Button(window, text = "LEICESTER CITY", bg = "white", command = lambda: parse_target("LEICESTER CITY"))
                buttEve = Button(window, text = "EVERTON", bg = "white", command = lambda: parse_target("EVERTON"))
                buttHam = Button(window, text = "WEST HAM", bg = "white", command = lambda: parse_target("WEST HAM"))
                buttTot = Button(window, text = "TOTTENHAM", bg = "white", command = lambda: parse_target("TOTTENHAM"))
                buttQpr = Button(window, text = "QPR", bg = "white", command = lambda: parse_target("QPR"))
                buttHull = Button(window, text = "HULL CITY", bg = "white", command = lambda: parse_target("HULL CITY"))
                buttSto = Button(window, text = "STOKE", bg = "white", command = lambda: parse_target("STOKE"))
                buttAst = Button(window, text = "ASTON VILLA", bg = "white", command = lambda: parse_target("ASTON VILLA"))
                buttArs = Button(window, text = "ARSENAL", bg = "white", command = lambda: parse_target("ARSENAL"))
                buttCry = Button(window, text = "CRYSTAL PALACE", bg = "white", command = lambda: parse_target("CRYSTAL PALACE"))
                buttLiv = Button(window, text = "LIVERPOOL", bg = "white", command = lambda: parse_target("LIVERPOOL"))
                buttSouth = Button(window, text = "SOUTHAMPTON", bg = "white", command = lambda: parse_target("SOUTHAMPTON"))
                buttNew = Button(window, text = "NEWCASTLE", bg = "white", command = lambda: parse_target("NEWCASTLE"))
                buttMancity = Button(window, text = "MAN CITY", bg = "white", command = lambda: parse_target( "MAN CITY"))
                buttBurn = Button(window, text = "BURNLEY", bg = "white", command = lambda: parse_target("BURNLEY"))
                buttChel = Button(window, text = "CHELSEA", bg = "white", command = lambda: parse_target("CHELSEA"))
                buttVisual = Button(window, text = "VISUALISATION", bg = "white", command = lambda: parse_target(""))

                labl.pack()
                buttVisual.pack()
                buttManutd.pack()
                buttSwan.pack()
                buttBrom.pack()
                buttSun.pack()
                buttLeic.pack()
                buttEve.pack()
                buttHam.pack()
                buttTot.pack()
                buttQpr.pack()
                buttHull.pack()
                buttSto.pack()
                buttAst.pack()
                buttArs.pack()
                buttCry.pack()
                buttLiv.pack()
                buttSouth.pack()
                buttNew.pack()
                buttMancity.pack()
                buttBurn.pack()
                buttChel.pack()
                window.mainloop()

                

            def parse_target(teamName):
                totalExcite = 0
                averageExcite = 0
                exciteArray = []
                
                with open("english premier league data.csv") as csv_file:
                    csvReader = csv.reader(csv_file, delimiter=",")
                    counter = 0
                    lineCount = 0
                    for row in csvReader:
                        if (teamName == ""):
                            averagePosition = 0
                        elif (teamName ==  "MAN CITY"):
                            averagePosition = 1
                        elif (teamName ==  "TOTTENHAM"):
                            averagePosition = 2
                        elif (teamName ==  "CHELSEA"):
                            averagePosition = 3
                        elif (teamName ==  "LIVERPOOL"):
                            averagePosition = 4
                        elif (teamName ==  "MAN UTD"):
                            averagePosition = 5
                        elif (teamName ==  "ARSENAL"):
                            averagePosition = 6
                        elif (teamName ==  "LEICESTER CITY"):
                            averagePosition = 8
                        elif (teamName ==  "EVERTON"):
                            averagePosition = 10
                        elif (teamName ==  "SOUTHAMPTON"):
                            averagePosition = 11
                        elif (teamName ==  "WEST HAM"):
                            averagePosition = 12
                        elif (teamName ==  "STOKE"):
                            averagePosition = 13
                        elif (teamName ==  "SWANSEA"):
                            averagePosition = 15
                        elif (teamName ==  "BURNLEY"):
                            averagePosition = 16
                        elif (teamName ==  "NEWCASTLE"):
                            averagePosition = 17
                        elif (teamName ==  "WEST BROM"):
                            averagePosition = 18
                        elif (teamName ==  "SUNDERLAND"):
                            averagePosition = 21
                        elif (teamName ==  "ASTON VILLA"):
                            averagePosition = 22
                        elif (teamName ==  "HULL CITY"):
                            averagePosition = 25
                        elif (teamName ==  "QPR"):
                            averagePosition = 27
                        elif (teamName ==  "CRYSTAL PALACE"):
                            averagePosition = 14

                        if lineCount == 0:
                            lineCount += 1
                        else:
                            counter = 0
                            totalExcite = 0
                            
                            while (row[1] or row[2] == teamName):
                                if row[1] or row[2] == teamName:
                                    exciteArray.append(row[5])
                                    print(exciteArray)
                                    break
                                else:
                                    break

                            for i in range(len(exciteArray)):
                                totalExcite = totalExcite + float(exciteArray[i])
                                counter += 1
                            averageExcite = totalExcite / counter
                            print(totalExcite)
                            print(counter)
                            
                            averageExcite = round(averageExcite, 2)
                            
                            
                        


                if (averagePosition > 0):
                    posString = f"s average position: {averagePosition} ,"
                else:
                    posString = "Overall"

                print(f'{teamName}{posString} average match excitement: {averageExcite}   ')
                
                    
                

            main()
        
                
        elif (choice == "2"):
            lineCount = 0
            v1 = 0
            v2 = 0
            with open("english premier league data.csv") as csv_file:
                    csvReader = csv.reader(csv_file, delimiter=",")
                    teamName = "MAN CITY"
                    for row in csvReader:
                        if (lineCount == 0):
                            lineCount += 1
                        else:
                            while (row[1] or row[2] == teamName):
                                v1 = float(row[5])
                                v2 = v1 + v2
                                
                                lineCount += 1
                                break
                             
                    
                    


        
        else:
            print ("Invalid input")
#page two-------------------------------------------------------------------------------------------------------
def page_two():
    key = 0
    print ("""-------------------PAGE2-------------------
    1) View Data
    0)EXIT
""")
    while key == 0:
        choice = input("""Please choose a page option: """)
        if choice == "0":
            key = 1
            menu()
        elif choice == "1":
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
        else:
            print ("Invalid input")

#page three------------------------------------------------------------------------------------------------------
def page_three():
    key = 0
    print("""-------------------PAGE3-------------------
    1) View Data
    0)EXIT
""")
    while key == 0:
        choice = input("""Please choose a page option: """)
        if choice == "0":
            key = 1
            menu()
        elif choice == "1":
            def choice(derby1, derby2):
                #window for data selection
                window = Tk()
                window.title("English Premier League")
                window.geometry("250x250")
                window.configure(background = "black")
                window.iconbitmap("favicon.ico")
                labl = Label(window, text = "Visualisation Choices", fg = "white", bg = "black")
                buttPos = Button(window, text = "Possession", bg = "white", command = lambda: parse(derby1, derby2, "Possession"))
                buttGoal = Button(window, text = "Goals", bg = "white", command = lambda: parse(derby1, derby2, "Goals"))
                buttCards = Button(window, text = "Cards", bg = "white", command = lambda: parse(derby1, derby2, "Cards"))

                labl.pack()
                buttPos.pack()
                buttGoal.pack()
                buttCards.pack()
                
                window.mainloop()
                
            def main():
                #window for team selection
                window = Tk()
                window.title("EPL Data")
                window.geometry("300x300")
                window.configure(background = "black")
                window.iconbitmap("favicon.ico")
                labl = Label(window, text = "English Premier League", fg = "white", bg = "black")
                buttMan = Button(window, text = "Manchester Derby", bg = "white", command = lambda: choice("MAN UTD", "MAN CITY"))
                buttLon = Button(window, text = "London Derby", bg = "white", command = lambda: choice("ARSENAL", "CHELSEA"))
                buttNor = Button(window, text = "North London Derby", bg = "white", command = lambda: choice("TOTTENHAM", "ARSENAL"))
                buttWes = Button(window, text = "West London Derby", bg = "white", command = lambda: choice("CHELSEA", "FULHAM"))
                buttMer = Button(window, text = "Merseyside Derby", bg = "white", command = lambda: choice("LIVERPOOL", "EVERTON"))
                buttTyn = Button(window, text = "Tyne-Wear Derby", bg = "white", command = lambda: choice("SUNDERLAND", "NEWCASTLE"))

                labl.pack()
                buttMan.pack()
                buttLon.pack()
                buttNor.pack()
                buttWes.pack()
                buttMer.pack()
                buttTyn.pack()
                
                window.mainloop()

            def parse(derby1, derby2, choice1):
                #parse derbies data
                #initialise arrays and variables for data parsing
                pos1 = []
                pos2 = []
                yellow1 = []
                yellow2 = []
                red1 = []
                red2 = []
                total = 0
                total2 = 0
                totalYellow1 = 0
                totalYellow2 = 0
                totalRed1 = 0
                totalRed2 = 0
            
                with open("english premier league data.csv") as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    line_count = 0
                    if choice1 == "Possession":
                        for row in csv_reader: #while csv still has unread lines
                            while (row[1] == derby1 or row[1] == derby2) and (row[2] == derby1 or row[2] == derby2): #for all rows containing selected teams
                                print(f'\t{row[1]} vs {row[2]} Score: {row[3]} Year: {row[40]}')#presents results of all teams in command line as extra info
                                if row[1] == derby1:
                                    pos1.append(row[8])#adds possession stats to array which will later be averaged
                                    pos2.append(row[9])
                                else:
                                    pos1.append(row[9])
                                    pos2.append(row[8])

                                line_count += 1#counts number of lines processed
                                break
                            
                        for i in range(len(pos1)):
                            total = total + int(pos1[i])
                            total2 = total2 + int(pos2[i])#calculates average possession
                        avg = total / len(pos1)
                        avg2 = total2 / len(pos2)
                        avg = round(avg, 2)
                        avg2 = round(avg2, 2)
                        pieVal = np.array([avg, avg2])#adds values to pie chart data array
                        labelList = [derby1 + "\n" + str(avg), derby2 + "\n" + str(avg2)]#prepares labels to be displayed on pie chart
                        print(derby1, "Average Possesion: ", avg)
                        print(derby2, "Average Possession", avg2)
                        print(f'Processed {line_count} lines.')
                        plt.title("Average Possession")
                        plt.pie(pieVal, labels = labelList, shadow = True) #creates pie chart using data calculated earlier
                        plt.show()

                    if choice1 == "Goals":
                        #same concept as first if
                        for row in csv_reader:
                            while (row[1] == derby1 or row[1] == derby2) and (row[2] == derby1 or row[2] == derby2):
                                print(f'\t{row[1]} vs {row[2]} Score: {row[3]} Year: {row[40]}')
                                if row[1] == derby1:
                                    pos1.append(row[36])
                                    pos2.append(row[37])
                                else:
                                    pos1.append(row[37])
                                    pos2.append(row[36])

                                line_count += 1
                                break
                            
                        for i in range(len(pos1)):
                            total = total + int(pos1[i])
                            total2 = total2 + int(pos2[i])
                        avg = total / len(pos1)
                        avg2 = total2 / len(pos2)
                        avg = round(avg, 2)
                        avg2 = round(avg2, 2)
                        pieVal = np.array([avg, avg2])
                        labelList = [derby1 + "\n" + str(avg), derby2 + "\n" + str(avg2)]
                        print(derby1, "Average Goals: ", avg)
                        print(derby2, "Average Goals:", avg2)
                        print(f'Processed {line_count} lines.')
                        plt.title("Average Goals")
                        plt.pie(pieVal, labels = labelList, shadow = True)
                        plt.show()

                    if choice1 == "Cards":
                        #same concept as previous 2 ifs
                        for row in csv_reader:
                            while (row[1] == derby1 or row[1] == derby2) and (row[2] == derby1 or row[2] == derby2):
                                print(f'\t{row[1]} vs {row[2]} Score: {row[3]} Year: {row[40]}')
                                if row[1] == derby1: 
                                    numYellow1 = float(row[21]) + float(row[22])#totals calculated seperately because it didnt work the normal way for some reason
                                    numYellow2 = float(row[34]) + float(row[35])
                                    yellow1.append(numYellow1)
                                    yellow2.append(numYellow2)
                                    red1.append(row[23])
                                    red2.append(row[36])
                                else:
                                    numYellow1 = float(row[21]) + float(row[22])
                                    numYellow2 = float(row[34]) + float(row[35])
                                    yellow2.append(numYellow1)
                                    yellow1.append(numYellow2)
                                    red2.append(row[23])
                                    red1.append(row[36])

                                line_count += 1
                                break
                            
                        for i in range(len(yellow1)):
                            totalYellow1 = totalYellow1 + float(yellow1[i])#calculates average number of red and yellow cards for selected derbies
                            totalYellow2 = totalYellow2 + float(yellow2[i])
                            totalRed1 = totalRed1 + float(red1[i])
                            totalRed2 = totalRed2 + float(red2[i])
                        avgYellow1 = totalYellow1 / len(yellow1)
                        avgYellow2 = totalYellow2 / len(yellow2)
                        avgRed = totalRed1 / len(red1)
                        avgRed2 = totalRed2 / len(red2)
                        avgYellow1 = round(avgYellow1, 2)#rounds average cards number to prevent long decimals
                        avgYellow2 = round(avgYellow2, 2)
                        avgRed = round(avgRed, 2)
                        avgRed = round(avgRed2, 2)
                        pieVal = np.array([avgYellow1, avgRed, avgYellow2, avgRed2])
                        labelList = [derby1 + " Red Cards\n" + str(avgYellow1), derby1 + " Yellow Cards\n" + str(avgRed), derby2 + " Red Cards\n" + str(avgYellow2), derby2 + " Yellow Cards\n" + str(avgRed2)]
                        print(derby1, "Average Red Cards: ", avgYellow1)
                        print(derby2, "Average Red Cards:", avgYellow2)
                        print(derby1, "Average Yellow Cards: ", avgRed)
                        print(derby2, "Average Yellow Cards: ", avgRed2)
                        print(f'Processed {line_count} lines.')
                        plt.title("Average Cards")
                        plt.pie(pieVal, labels = labelList, shadow = True)
                        plt.show()

            main()
            
        
    else:
        print ("Invalid input")
#page four-------------------------------------------------------------------------------------------------------
def page_four():
    key = 0
    print ("""-------------------PAGE4-------------------
    1) View Data
    0)EXIT
""")
    while key == 0:
        choice = input("""Please choose a page option: """)
        if choice == "0":
            key = 1
            menu()
        elif choice == "1":
            print(".")
        else:
            print ("Invalid input")
#page five------------------------------------------------------------------------------------------------------
def page_five():
    
    key = 0
    print ("""-------------------PAGE5-------------------
    1) View Data
    0) EXIT
""")
    while key == 0:
        choice = input("""Please choose a page option: """)
        if choice == "0":
            key = 1
            menu()
        elif choice == "1":
            Teams1 = ['Man City', 'Liverpool', 'Chelsea', 'Tottenham', 'Arsenal', 'Man United', 'Wolves', 'Everton', 'Leicester', 'West Ham', 'Watford', 'Crystal Palace', 'Newcastle', 'Bournemouth', 'Burnley', 'Southampton', 'Brighton', 'Cardiff City', 'Fulham', 'Huddersfield']
            Points1 = [98, 97, 72, 71, 70, 66, 57, 54, 52, 52, 50, 49, 45, 45, 40, 39, 36, 34, 26, 16]

            Teams2 = ['Liverpool', 'Man City', 'Man United', 'Chelsea', 'Leicester', 'Tottenham', 'Wolves', 'Arsenal', 'Sheffield', 'Burnley', 'Southampton', 'Everton', 'Newcastle', 'Crystal Palace', 'Brighton', 'West Ham', 'Aston Villa', 'Bournemouth', 'Watford', 'Norwich City']
            Points2 = [99, 81, 66, 66, 62, 59, 59, 56, 54, 54, 52, 49, 44, 43, 41, 39, 35, 34, 34, 21]

            Teams3 = ['Man City', 'Man United', 'Liverpool', 'Chelsea', 'Leicester', 'West Ham', 'Tottenham', 'Arsenal', 'Leeds', 'Everton', 'Aston Villa', 'Newcastle', 'Wolves', 'Crystal Palace', 'Southampton', 'Brighton', 'Burnley', 'Fulham', 'West Brom', 'Sheffield']
            Points3 = [86, 74, 69, 67, 66, 65, 62, 61, 59, 59, 55, 45, 45, 44, 43, 41, 39, 28, 26, 23]
            #Declaring all of the teams and the points that they recieved in that season

            def choose():
                print("Please choose what season you would like to view:")
                print("[1] 2018/19")
                print("[2] 2019/20")
                print("[3] 2020/21")
                # Text based menu that allows the user to choose what season they would like to view


            choose()
            option1 = int(input("Please enter your option: "))

            while option1 != 0:
                if option1 == 1:
                    print("Premier League Table 2018/19")
                    print("Please choose what type of data visualisation you would like to see:")
                    print("[1] Bar Chart")
                    print("[2] Pie Chart")
                    print("[0] Exit the program.")
                    # Text based menu thats allows the user to choose what type of visualisation they would like to view


                    option2 = int(input("Please enter your option: "))

                    while option2 != 0:
                        if option2 == 1:
                        # This option will display a visualisation of a bar chart
                            plt.bar(Teams1, Points1)
                            plt.title('Premier League Table 2018/19 Season')
                            plt.xlabel('Teams')
                            plt.ylabel('Points')
                            plt.show()  
                            plt.show(block=False)
                            plt.close('all')                           

                        elif option2 == 2:
                        # This option will display a visualisation of a pie chart which displays the distribution of all points added up in the premier league table
                            fig1 = plt.figure()
                            ax1 = fig1.add_axes([0,0,1,1])
                            ax1.axis('equal')
                            ax1.pie(Points1, labels1 = Teams1,autopct='%.2f%%')
                            plt.show()
                        else:
                            print("Invalid option, please try again.")

                    print()    
                    option2 = int(input("Please enter your option: "))
                    plt.close(all)

                elif option1 == 2:

                    print("Premier League Table 2019/20")
                    print("Please choose what type of data visualisation you would like to see:")
                    print("[1] Bar Chart")
                    print("[2] Pie Chart")
                    print("[0] Exit the program.")
                    # Text based menu thats allows the user to input an option


                    option3 = int(input("Please enter your option: "))

                    while option3 != 0:
                        if option3 == 1:
                        # This option will display a visualisation of a bar chart
                            plt.bar(Teams2, Points2)
                            plt.title('Premier League Table 2019/20 Season')
                            plt.xlabel('Teams')
                            plt.ylabel('Points')
                            plt.show()

                        elif option3 == 2:
                        # his option will display a visualisation of a pie chart which displays the distribution of all points in the premier league table
                            fig2 = plt.figure()
                            ax2 = fig2.add_axes([0,0,1,1])
                            ax2.axis('equal')
                            ax2.pie(Points2, labels2 = Teams2,autopct='%.2f%%')
                            plt.show()
                        else:
                            print("Invalid option, please try again.")

                    print()        
                    option3 = int(input("Please enter your option: "))

                elif option1 == 3:
                    print("Premier League Table 2020/21")
                    print("Please choose what type of data visualisation you would like to see:")
                    print("[1] Bar Chart")
                    print("[2] Pie Chart")
                    print("[0] Exit the program.")
                    # Text based menu thats allows the user to input an option


                    option4 = int(input("Please enter your option: "))

                    while option4 != 0:
                        if option4 == 1:
                        # This option will display a visualisation of a bar chart
                            plt.bar(Teams3, Points3)
                            plt.title('Premier League Table 2020/21 Season')
                            plt.xlabel('Teams')
                            plt.ylabel('Points')
                            plt.show()

                        elif option4 == 2:
                        # This option will display a visualisation of a pie chart which displays the distribution of all points in the premier league table
                            fig3 = plt.figure()
                            ax3 = fig3.add_axes([0,0,1,1])
                            ax3.axis('equal')
                            ax3.pie(Points3, labels3 = Teams3,autopct='%.2f%%')
                            plt.show()
                        else:
                            print("Invalid option, please try again.")

                    print()        
                    option4 = int(input("Please enter your option: "))

                else:
                    print("Invalid option, please try again.")
                    # While loop if none of the requested input is given

                print()
                choose()
                option1 = int(input("Please enter your option: "))




            plt.close('all')
        else:
            print ("Invalid input")
#page six------------------------------------------------------------------------------------------------------
def page_six():
    key = 0
    print ("""-------------------PAGE6-------------------
    1) View Data
    0)EXIT
""")
    while key == 0:
        choice = input("""Please choose a page option: """)
        if choice == "0":
            key = 1
            menu()
        elif choice == "1":
            font = {'family' : 'normal',
                    'weight' : 'bold',
                    'size'   : 6}

            matplotlib.rc('font', **font)

            #Defines the subroutine csvimport
            def csvimport():
                
                
                
                #Opens the csv file and creates a reader that puts the lines into a list variable
                with open('english premier league data.csv', 'r') as csvfile:
                    
                    
                    lines = csvfile.readlines()

                    #Creates all variables needed for the program 
                    goals = []
                    titles = [20,6,7,13,19,2,1,9,7,0,0,4,3,0,0,0,3,0,2,0]
                    MANUTD = 0
                    CHEAL = 0
                    MANCIT = 0
                    ARSENAL = 0
                    LIVERPOOL = 0
                    SPURS = 0
                    LEISTER = 0
                    EVERTON = 0
                    VILLA = 0
                    SOUTHHAMPT = 0
                    WESTHAM = 0
                    NEWCASTLE = 0
                    WOLVES = 0
                    WATFORD = 0
                    CRYSTAL = 0
                    NORWICH = 0
                    LEEDS = 0
                    BRIGHTON = 0
                    BURNLEY = 0
                    WESTBROM = 0
                    


                    for line in lines:
                        data = line.split(',')
                        if (data[1]) == "MAN UTD":
                            MANUTD = MANUTD + int(data[36])
                        elif (data[1]) == "CHELSEA":
                            CHEAL = CHEAL + int(data[36])
                        
                        elif (data[1]) == "MAN CITY":
                            MANCIT = MANCIT + int(data[36])
                            
                        elif (data[1]) == "ARSENAL":
                            ARSENAL = ARSENAL + int(data[36])
                            
                        elif (data[1]) == "LIVERPOOL":
                            LIVERPOOL = LIVERPOOL + int(data[36])
                            
                        elif (data[1]) == "TOTTENHAM":
                            SPURS = SPURS + int(data[36])
                            
                        elif (data[1]) == "LEICESTER CITY":
                            LEISTER = LEISTER + int(data[36])
                        
                        elif (data[1]) == "EVERTON":
                            EVERTON = EVERTON + int(data[36])
                            
                        elif (data[1]) == "ASTON VILLA":
                            VILLA = VILLA + int(data[36])
                            
                        elif (data[1]) == "SOUTHHAMPTON":
                            SOUTHHAMPT = SOUTHHAMPT + int(data[36])
                            
                        elif (data[1]) == "WEST HAM":
                            WESTHAM = WESTHAM + int(data[36])
                            
                        elif (data[1]) == "NEWCASTLE":
                            NEWCASTLE = NEWCASTLE + int(data[36])
                            
                        elif (data[1]) == "WOLVES":
                            WOLVES = WOLVES + int(data[36])
                            
                        elif (data[1]) == "WATFORD":
                            WATFORD = WATFORD + int(data[36])
                        
                        elif (data[1]) == "CRYSTAL PALACE":
                            CRYSTAL = CRYSTAL + int(data[36])
                        
                        elif (data[1]) == "NORWICH":
                            NORWICH = NORWICH + int(data[36])
                        
                        elif (data[1]) == "LEEDS UTD":
                            LEEDS = LEEDS + int(data[36])
                            
                        elif (data[1]) == "BRIGHTON":
                            BRIGHTON = BRIGHTON + int(data[36])
                            
                        elif (data[1]) == "BURNLEY":
                            BURNLEY = BURNLEY + int(data[36])
                            
                        elif (data[1]) == "WEST BROM":
                            WESTBROM = WESTBROM + int(data[36])

                        if (data[2]) == "MAN UTD":
                            MANUTD = MANUTD + int(data[37])
                        elif (data[2]) == "CHELSEA":
                            CHEAL = CHEAL + int(data[37])
                        
                        elif (data[2]) == "MAN CITY":
                            MANCIT = MANCIT + int(data[37])
                            
                        elif (data[2]) == "ARSENAL":
                            ARSENAL = ARSENAL + int(data[37])
                            
                        elif (data[2]) == "LIVERPOOL":
                            LIVERPOOL = LIVERPOOL + int(data[37])
                            
                        elif (data[2]) == "TOTTENHAM":
                            SPURS = SPURS + int(data[37])
                            
                        elif (data[2]) == "LEICESTER CITY":
                            LEISTER = LEISTER + int(data[37])
                        
                        elif (data[2]) == "EVERTON":
                            EVERTON = EVERTON + int(data[37])
                            
                        elif (data[2]) == "ASTON VILLA":
                            VILLA = VILLA + int(data[37])
                            
                        elif (data[2]) == "SOUTHAMPTON":
                            SOUTHHAMPT = SOUTHHAMPT + int(data[37])
                            
                        elif (data[2]) == "WEST HAM":
                            WESTHAM = WESTHAM + int(data[37])
                            
                        elif (data[2]) == "NEWCASTLE":
                            NEWCASTLE = NEWCASTLE + int(data[37])
                            
                        elif (data[2]) == "WOLVES":
                            WOLVES = WOLVES + int(data[37])
                            
                        elif (data[2]) == "WATFORD":
                            WATFORD = WATFORD + int(data[37])
                        
                        elif (data[2]) == "CRYSTAL PALACE":
                            CRYSTAL = CRYSTAL + int(data[37])
                        
                        elif (data[2]) == "NORWICH":
                            NORWICH = NORWICH + int(data[37])
                        
                        elif (data[2]) == "LEEDS UTD":
                            LEEDS = LEEDS + int(data[37])
                            
                        elif (data[2]) == "BRIGHTON":
                            BRIGHTON = BRIGHTON + int(data[37])
                            
                        elif (data[2]) == "BURNLEY":
                            BURNLEY = BURNLEY + int(data[37])
                            
                        elif (data[2]) == "WEST BROM":
                            WESTBROM = WESTBROM + int(data[37])
                            

                


                    
                goals.append(MANUTD/50)
                goals.append(CHEAL/50)
                goals.append(MANCIT/50)
                goals.append(ARSENAL/50)
                goals.append(LIVERPOOL/50)
                goals.append(SPURS/50)
                goals.append(LEISTER/50)
                goals.append(EVERTON/50)
                goals.append(VILLA/50)
                goals.append(SOUTHHAMPT/50)
                goals.append(WESTHAM/50)
                goals.append(NEWCASTLE/50)
                goals.append(WOLVES/50)
                goals.append(WATFORD/50)
                goals.append(CRYSTAL/50)
                goals.append(NORWICH/50)
                goals.append(LEEDS/50)
                goals.append(BRIGHTON/50)
                goals.append(BURNLEY/50)
                goals.append(WESTBROM/50)

                #Prints list of csv cells
                
                
                x = np.arange(20)
                y1 = goals
                y2 = titles
                width = 0.4
                    
                    
                plt.bar(x-0.2, y1, width)
                plt.bar(x+0.2, y2, width)
                plt.xticks(x, ['MAN UTD', 'CHELSEA', 'MAN CITY', 'ARSENAL', 'LPOOL', 'SPURS', 'LEICESTER', 'EVERTON', 'ASTON VILLA', 'SHAMPTON', 'WEST HAM', 'NEWCASTLE', 'WOLVES', 'WATFORD', 'CRYSTAL PALACE', 'NORWICH', 'LEEDS', 'BRIGHTON', 'BURNLEY', 'BRENTFORD'])
                plt.xlabel("Teams (In order of popularity)")
                plt.ylabel("Goals Scored in multiples of 50 (Blue) Titles Won (Orange)")
                


                plt.show()


                    
                    
                
                
            #Defines the subroutine main
            def main():
                #Creates a loop for the main menu
                loop = "0"
                while loop == "0":

                    #Accepts user input to choose from the menu options - Uses numbers so capitals dont matter - Could also use .Upper() function
                    userChoice = input("------Menu------\n\n1. Read csv file\n\n2. Exit\n\n")
                    if userChoice == "1":
                        csvimport()
                        print("\n\nSelect another option: \n")
                    elif userChoice == "2":
                        print("Quitting...")
                        loop = "1"
                    else:
                        print("\n\nInvalid input! Try again: \n\n")


            #Calls the main menu subroutine 
            main()
        else:
            print ("Invalid input")


            
        
    

#main menu-------------------------------------------------------------------------------------------------------    
def menu():
    print ("""-------------------MENU-------------------
    1) Excitement vs League Position
    2) Top vs Bttom League Comparison
    3) Derby Stats
    4) Half Time VS End
    5) Points Per Season
    6) Popularity vs Result
    0) EXIT
    """)
    main_choice()
def main_choice():   
    choose = input("Please choose a menu option: ")
    if choose == "1":
        print ("001")
        page_one()
    elif choose == "2":
        print ("010")
        page_two()
    elif choose == "3":
        print ("011")
        page_three()
    elif choose == "4":
        print ("100")
        page_four()
    elif choose == "5":
        print ("101")
        page_five()
    elif choose == "6":
        print ("110")
        page_six()
    elif choose == "0":
        exit()
    else:
        print ("error")
        main_choice()

menu()
