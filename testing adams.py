#imports---------------------------------------------------------------------------------------------------------
from tkinter import *
import csv
from unicodedata import decimal
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
                key = 0
                teamNameList = ["MAN CITY","TOTTENHAM", "CHELSEA","LIVERPOOL", "MAN UTD", "ARSENAL", "LEICESTER","EVERTON", "SOUTHAMPTON", "WEST HAM","STOKE", "SWANSEA", "BURNLEY","NEWCASTLE", "WEST BROM", "SUNDERLAND", "ASTON VILLA", "HULL CITY", "QPR", "CRYSTAL PALACE"]
                
                with open("english premier league data.csv") as csv_file:
                    csvReader = csv.reader(csv_file, delimiter=",")
                    next(csvReader)
                    exciteCount = 0.00
                    excite = 0.00
                    
                                
                        

                    for row in csvReader:
                        
                        if (teamName ==  "MAN CITY"):
                            if row[5] == "Match Excitement":
                                pass
                            elif type(row[5]) == str:
                                pass
                            averagePosition = 1
                            exciteCount = exciteCount + 1
                            excite = excite + float(row[5])
                        elif (teamName ==  "TOTTENHAM"):
                            averagePosition = 2
                            if row[5] == "Match Excitement":
                                pass
                            exciteCount = exciteCount + 1
                            excite = excite + float(row[5])
                        elif (teamName ==  "CHELSEA"):
                            averagePosition = 3
                            if row[5] == "Match Excitement":
                                pass
                            exciteCount = exciteCount + 1
                            excite = excite + float(row[5])
                        elif (teamName ==  "LIVERPOOL"):
                            averagePosition = 4
                            if row[5] == "Match Excitement":
                                pass
                            exciteCount = exciteCount + 1
                            excite = excite + float(row[5])
                        elif (teamName ==  "MAN UTD"):
                            averagePosition = 5
                            if row[5] == "Match Excitement":
                                pass
                            exciteCount = exciteCount + 1
                            excite = excite + float(row[5])
                        elif (teamName ==  "ARSENAL"):
                            averagePosition = 6
                            if row[5] == "Match Excitement":
                                pass
                            exciteCount = exciteCount + 1
                            excite = excite + float(row[5])
                        elif (teamName ==  "LEICESTER CITY"):
                            averagePosition = 8
                            if row[5] == "Match Excitement":
                                pass
                            exciteCount = exciteCount + 1
                            excite = excite + float(row[5])
                        elif (teamName ==  "EVERTON"):
                            averagePosition = 10
                            if row[5] == "Match Excitement":
                                pass
                            exciteCount = exciteCount + 1
                            excite = excite + float(row[5])
                        elif (teamName ==  "SOUTHAMPTON"):
                            averagePosition = 11
                            if row[5] == "Match Excitement":
                                pass
                            exciteCount = exciteCount + 1
                            excite = excite + float(row[5])
                        elif (teamName ==  "WEST HAM"):
                            averagePosition = 12
                            if row[5] == "Match Excitement":
                                pass
                            exciteCount = exciteCount + 1
                            excite = excite + float(row[5])
                        elif (teamName ==  "STOKE"):
                            averagePosition = 13
                            if row[5] == "Match Excitement":
                                pass
                            exciteCount = exciteCount + 1
                            excite = excite + float(row[5])
                        elif (teamName ==  "SWANSEA"):
                            averagePosition = 15
                            if row[5] == "Match Excitement":
                                pass
                            exciteCount = exciteCount + 1
                            excite = excite + float(row[5])
                        elif (teamName ==  "BURNLEY"):
                            averagePosition = 16
                            if row[5] == "Match Excitement":
                                pass
                            exciteCount = exciteCount + 1
                            excite = excite + float(row[5])
                        elif (teamName ==  "NEWCASTLE"):
                            averagePosition = 17
                            if row[5] == "Match Excitement":
                                pass
                            exciteCount = exciteCount + 1
                            excite = excite + float(row[5])
                        elif (teamName ==  "WEST BROM"):
                            averagePosition = 18
                            if row[5] == "Match Excitement":
                                pass
                            exciteCount = exciteCount + 1
                            excite = excite + float(row[5])
                        elif (teamName ==  "SUNDERLAND"):
                            averagePosition = 21
                            if row[5] == "Match Excitement":
                                pass
                            exciteCount = exciteCount + 1
                            excite = excite + float(row[5])
                        elif (teamName ==  "ASTON VILLA"):
                            averagePosition = 22
                            if row[5] == "Match Excitement":
                                pass
                            exciteCount = exciteCount + 1
                            excite = excite + float(row[5])
                        elif (teamName ==  "HULL CITY"):
                            averagePosition = 25
                            if row[5] == "Match Excitement":
                                pass
                            exciteCount = exciteCount + 1
                            excite = excite + float(row[5])
                        elif (teamName ==  "QPR"):
                            averagePosition = 27
                            if row[5] == "Match Excitement":
                                pass
                            exciteCount = exciteCount + 1
                            excite = excite + float(row[5])
                        elif (teamName ==  "CRYSTAL PALACE"):
                            averagePosition = 14
                            if row[5] == "Match Excitement":
                                pass
                            exciteCount = exciteCount + 1
                            excite = excite + float(row[5])
                        n= []

                    print ("Average excitement: " + str(excite/exciteCount))
                        


                
                    
                

            main()
        
                
                

        
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
