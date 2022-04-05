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
                #creates tkinter window
                window = Tk()
                window.iconbitmap("favicon.ico")
                window.title("EPL Data")
                window.geometry("300x600")
                window.configure(background = "black")
                #defines buttons
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
                #applies buttons to window
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

                
            finds the information for the relevant team
            def parse_target(teamName):
                totalExcite = 0
                averageExcite = 0
                exciteArray = []
                
                with open("english premier league data.csv") as csv_file:
                    csvReader = csv.reader(csv_file, delimiter=",")
                    counter = 0
                    lineCount = 0
                    for row in csvReader:
                        #declares the league position of each team
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
                        #stops from reading titles instead of data
                        if lineCount == 0:
                            lineCount += 1
                        else:
                            counter = 0
                            totalExcite = 0
                            #works out average "excitement" for chosen team   
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
            teams = ["MC","TT","LP","MU","AR","LC","EV","SH","WH","SK","CP","SS","NC","WB","SL","AV","HC","QPR"
            data = [1,2 3,4 5,6 8,10,11,12,13,14,15,16,17,18,21,22,25,27]
            plt.title("league positions in order of attendance
            plt.bar(teams, data)
            plt.show()
                             
                    
                    


        
        else:
            print ("Invalid input")
