#imports---------------------------------------------------------------------------------------------------------
from tkinter import *
import csv
import numpy as np
import matplotlib.pyplot as plt
#page one--------------------------------------------------------------------------------------------------------
def page_one():
    key = 0
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
                window.title("EPL Data")
                window.geometry("300x550")
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
                
                labl.pack()
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
                key = 0
                
                with open("english premier league data.csv") as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=",")
                    lineCount = 0
                    counter = 0
                    target = 0
                    target1 = 0
                    for row in csv_reader:
                        while key == 0:
                            if ({row[1]} == teamName):
                                target = target + int(row[11])
                            elif ({row[2]} == teamName):
                                target = target + int(row[11]) 
                            else:
                                key = 1
                    print (target)
                    print ({row[11]})
                        #while ({row[1]} or {row[2]} == teamName):
                         #   if ({row[1]} == teamName):
                          #      target1 = row[11]
                           # elif({row[2]} == teamName):
                            #    target1 = row[24]
                            #target0 = target0 + target1
                            #counter = counter + 1
                            #lineCount += 1
                            #break
                        #targetAverage = target0 / counter
                #print(f'\t{teamName}, position , {targetAverage}   ')
                    
                
            main()
        elif (choice == "2"):
            plt.figure(figsize=(8, 5), dpi=80)
            plt.subplot(111)

            X = np.linspace(-np.pi, np.pi, 256)
            C = np.cos(X)
            S = np.sin(X)

            plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-")
            plt.plot(X, S, color="red", linewidth=2.5, linestyle="-")

            plt.xlim(X.min() * 1.1, X.max() * 1.1)
            plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
                    [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

            plt.ylim(C.min() * 1.1, C.max() * 1.1)
            plt.yticks([-1, 0, +1],
                    [r'$-1$', r'$0$', r'$+1$'])

            plt.show()
        
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
            print(".")
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
                        for row in csv_reader:
                            while (row[1] == derby1 or row[1] == derby2) and (row[2] == derby1 or row[2] == derby2):
                                print(f'\t{row[1]} vs {row[2]} Score: {row[3]} Year: {row[40]}')
                                if row[1] == derby1:
                                    pos1.append(row[8])
                                    pos2.append(row[9])
                                else:
                                    pos1.append(row[9])
                                    pos2.append(row[8])

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
                        print(derby1, "Average Possesion: ", avg)
                        print(derby2, "Average Possession", avg2)
                        print(f'Processed {line_count} lines.')
                        plt.title("Average Possession")
                        plt.pie(pieVal, labels = labelList, shadow = True)
                        plt.show()

                    if choice1 == "Goals":
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
                        for row in csv_reader:
                            while (row[1] == derby1 or row[1] == derby2) and (row[2] == derby1 or row[2] == derby2):
                                print(f'\t{row[1]} vs {row[2]} Score: {row[3]} Year: {row[40]}')
                                if row[1] == derby1: 
                                    yellow1.append(float(row[21]) + float(row[22]))
                                    yellow2.append(float(row[34]) + float(row[35]))
                                    red1.append(row[23])
                                    red2.append(row[36])
                                else:
                                    yellow2.append(row[21] + row[22])
                                    yellow1.append(row[34] + row[35])
                                    red2.append(row[23])
                                    red1.append(row[36])

                                line_count += 1
                                break
                            
                        for i in range(len(yellow1)):
                            totalYellow1 = totalYellow1 + int(yellow1[i])
                            totalYellow2 = totalYellow2 + int(yellow2[i])
                            totalRed1 = totalRed1 + int(red1[i])
                            totalRed2 = totalRed2 + int(red2[i])
                        avgYellow1 = totalYellow1 / len(yellow1)
                        avgYellow2 = totalYellow2 / len(yellow2)
                        avgRed = totalRed1 / len(red1)
                        avgRed2 = totalRed2 / len(red2)
                        avgYellow1 = round(avgYellow1, 2)
                        avgYellow2 = round(avgYellow2, 2)
                        avgRed = round(avgRed, 2)
                        avgRed = round(avgRed2, 2)
                        pieVal = np.array([avgYellow1, avgRed, avgYellow2, avgRed2])
                        labelList = [derby1 + " Yellow Cards\n" + str(avgYellow1), derby1 + " Red Cards\n" + str(avgRed), derby2 + " Yellow Cards\n" + str(avgYellow2), derby2 + " Red Cards\n" + str(avgRed2)]
                        print(derby1, "Average Yellow Cards: ", avgYellow1)
                        print(derby2, "Average Yellow Cards:", avgYellow2)
                        print(derby1, "Average Red Cards: ", avgRed)
                        print(derby2, "Average Red Cards: ", avgRed2)
                        print(f'Processed {line_count} lines.')
                        plt.title("Average Goals")
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
#page six------------------------------------------------------------------------------------------------------
def page_six():
    key = 0
    print ("""-------------------PAGE6-------------------
    1) Visual Representation
    2) Written Representation
    0)EXIT
""")
    while key == 0:
        choice = input("""Please choose a page option: """)
        if choice == "0":
            key = 1
            menu()
        elif choice == "1":
            (".")
        else:
            print ("Invalid input")


            
        
    

#main menu-------------------------------------------------------------------------------------------------------    
def menu():
    print ("""-------------------MENU-------------------
    1) Target Shots vs Position
    2) Top vs Bttom League Comparison
    3) Rivals VS Average
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
