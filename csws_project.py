#imports---------------------------------------------------------------------------------------------------------
from tkinter import *
import csv
#page one--------------------------------------------------------------------------------------------------------
def page_one():
    key = 0
    print ("""-------------------PAGE1-------------------
    1) View Data
    0)EXIT
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
                buttMan = Button(window, text = "MAN UTD", bg = "white", command = lambda: parse_target(""))
                buttSwan = Button(window, text = "SWANSEA", bg = "white", command = lambda: parse_target(""))
                buttBrom = Button(window, text = "WEST BROM", bg = "white", command = lambda: parse_target(""))
                buttSun = Button(window, text = "SUNDERLAND", bg = "white", command = lambda: parse_target(""))
                buttLeic = Button(window, text = "LEICESTER CITY", bg = "white", command = lambda: parse_target(""))
                buttEve = Button(window, text = "EVERTON", bg = "white", command = lambda: parse_target(""))
                buttHam = Button(window, text = "WEST HAM", bg = "white", command = lambda: parse_target(""))
                buttTot = Button(window, text = "TOTTENHAM", bg = "white", command = lambda: parse_target(""))
                buttQpr = Button(window, text = "QPR", bg = "white", command = lambda: parse_target(""))
                buttHull = Button(window, text = "HULL CITY", bg = "white", command = lambda: parse_target(""))
                buttSto = Button(window, text = "STOKE", bg = "white", command = lambda: parse_target(""))
                buttAst = Button(window, text = "ASTON VILLA", bg = "white", command = lambda: parse_target(""))
                buttArs = Button(window, text = "ARSENAL", bg = "white", command = lambda: parse_target(""))
                buttCry = Button(window, text = "CRYSTAL PALACE", bg = "white", command = lambda: parse_target(""))
                buttLiv = Button(window, text = "LIVERPOOL", bg = "white", command = lambda: parse_target(""))
                buttSouth = Button(window, text = "SOUTHAMPTON", bg = "white", command = lambda: parse_target(""))
                buttNew = Button(window, text = "NEWCASTLE", bg = "white", command = lambda: parse_target(""))
                buttMan = Button(window, text = "MAN CITY", bg = "white", command = lambda: parse_target(""))
                buttBurn = Button(window, text = "BURNLEY", bg = "white", command = lambda: parse_target(""))
                buttChel = Button(window, text = "CHELSEA", bg = "white", command = lambda: parse_target(""))
                
                labl.pack()
                buttMan.pack()
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
                buttMan.pack()
                buttBurn.pack()
                buttChel.pack()
                
                window.mainloop()
            def parse_target():
                Team_name = []
                with open("english premier league data.csv") as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    line_count = 0
                    for row in csv_reader:
                        while (row[1] == Team_name or row[2] == Team_name):
                            print(f'\t{Team_name} in {row[40]}, postion:     ,:  ')
                            if row[1] == Team_name:
                                
                                

                            line_count += 1
                            break
                    for i in range(len(pos1)):
                        total = total + int(pos1[i])
                        total2 = total2 + int(pos2[i])
                    avg = total / len(pos1)
                    avg2 = total2 / len(pos2)
                    avg = round(avg, 2)
                    avg2 = round(avg2, 2)
                    print(derby1, "Average Possesion: ", avg)
                    print(derby2, "Average Possession", avg2)
                    print(f'Processed {line_count} lines.')
                
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
            def main():
                window = Tk()
                window.title("")
                window.geometry("250x250")
                window.configure(background = "black")
                labl = Label(window, text = "", fg = "white", bg = "black")
                buttEPL = Button(window, text = "", bg = "white", command = lambda: epl())

                labl.pack()
                buttEPL.pack()
                
                window.mainloop()
            def epl():
                window = Tk()
                window.title("EPL Data")
                window.geometry("300x300")
                window.configure(background = "black")
                labl = Label(window, text = "", fg = "white", bg = "black")
                buttMan = Button(window, text = "", bg = "white", command = lambda: parse("", ""))
                buttLon = Button(window, text = "", bg = "white", command = lambda: parse("", ""))
                buttNor = Button(window, text = "", bg = "white", command = lambda: parse("", ""))
                buttWes = Button(window, text = "", bg = "white", command = lambda: parse("", ""))
                buttMer = Button(window, text = "", bg = "white", command = lambda: parse("", ""))
                buttTyn = Button(window, text = "", bg = "white", command = lambda: parse("", ""))

                labl.pack()
                buttMan.pack()
                buttLon.pack()
                buttNor.pack()
                buttWes.pack()
                buttMer.pack()
                buttTyn.pack()
                
                window.mainloop()

            def parse(derby1, derby2):
                pos1 = []
                pos2 = []
                total = 0
                total2 = 0
                with open("english premier league data.csv") as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    line_count = 0
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
                    print(derby1, "Average Possesion: ", avg)
                    print(derby2, "Average Possession", avg2)
                    print(f'Processed {line_count} lines.')

        main()
            
        
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
            def main():
                window = Tk()
                window.title("European Derbys Data")
                window.geometry("250x250")
                window.configure(background = "black")
                labl = Label(window, text = "European Leagues", fg = "white", bg = "black")
                buttEPL = Button(window, text = "English Premier League", bg = "white", command = lambda: epl())

                labl.pack()
                buttEPL.pack()
                
                window.mainloop()
            def epl():
                window = Tk()
                window.title("EPL Data")
                window.geometry("300x300")
                window.configure(background = "black")
                labl = Label(window, text = "English Premier League", fg = "white", bg = "black")
                buttMan = Button(window, text = "Manchester Derby", bg = "white", command = lambda: parse("MAN UTD", "MAN CITY"))
                buttLon = Button(window, text = "London Derby", bg = "white", command = lambda: parse("ARSENAL", "CHELSEA"))
                buttNor = Button(window, text = "North London Derby", bg = "white", command = lambda: parse("TOTTENHAM", "ARSENAL"))
                buttWes = Button(window, text = "West London Derby", bg = "white", command = lambda: parse("CHELSEA", "FULHAM"))
                buttMer = Button(window, text = "Merseyside Derby", bg = "white", command = lambda: parse("LIVERPOOL", "EVERTON"))
                buttTyn = Button(window, text = "Tyne-Wear Derby", bg = "white", command = lambda: parse("SUNDERLAND", "NEWCASTLE"))

                labl.pack()
                buttMan.pack()
                buttLon.pack()
                buttNor.pack()
                buttWes.pack()
                buttMer.pack()
                buttTyn.pack()
                
                window.mainloop()

            def parse(derby1, derby2):
                pos1 = []
                pos2 = []
                total = 0
                total2 = 0
                with open("english premier league data.csv") as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    line_count = 0
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
                    print(derby1, "Average Possesion: ", avg)
                    print(derby2, "Average Possession", avg2)
                    print(f'Processed {line_count} lines.')

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
            def main():
                window = Tk()
                window.title("")
                window.geometry("250x250")
                window.configure(background = "black")
                labl = Label(window, text = "", fg = "white", bg = "black")
                buttEPL = Button(window, text = "", bg = "white", command = lambda: epl())

                labl.pack()
                buttEPL.pack()
                
                window.mainloop()
            def epl():
                window = Tk()
                window.title("EPL Data")
                window.geometry("300x300")
                window.configure(background = "black")
                labl = Label(window, text = "", fg = "white", bg = "black")
                buttMan = Button(window, text = "", bg = "white", command = lambda: parse("", ""))
                buttLon = Button(window, text = "", bg = "white", command = lambda: parse("", ""))
                buttNor = Button(window, text = "", bg = "white", command = lambda: parse("", ""))
                buttWes = Button(window, text = "", bg = "white", command = lambda: parse("", ""))
                buttMer = Button(window, text = "", bg = "white", command = lambda: parse("", ""))
                buttTyn = Button(window, text = "", bg = "white", command = lambda: parse("", ""))

                labl.pack()
                buttMan.pack()
                buttLon.pack()
                buttNor.pack()
                buttWes.pack()
                buttMer.pack()
                buttTyn.pack()
                
                window.mainloop()

            def parse(derby1, derby2):
                pos1 = []
                pos2 = []
                total = 0
                total2 = 0
                with open("english premier league data.csv") as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    line_count = 0
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
                    print(derby1, "Average Possesion: ", avg)
                    print(derby2, "Average Possession", avg2)
                    print(f'Processed {line_count} lines.')

        main()
            
        
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
            def main():
                window = Tk()
                window.title("")
                window.geometry("250x250")
                window.configure(background = "black")
                labl = Label(window, text = "", fg = "white", bg = "black")
                buttEPL = Button(window, text = "", bg = "white", command = lambda: epl())

                labl.pack()
                buttEPL.pack()
                
                window.mainloop()
            def epl():
                window = Tk()
                window.title("EPL Data")
                window.geometry("300x300")
                window.configure(background = "black")
                labl = Label(window, text = "", fg = "white", bg = "black")
                buttMan = Button(window, text = "", bg = "white", command = lambda: parse("", ""))
                buttLon = Button(window, text = "", bg = "white", command = lambda: parse("", ""))
                buttNor = Button(window, text = "", bg = "white", command = lambda: parse("", ""))
                buttWes = Button(window, text = "", bg = "white", command = lambda: parse("", ""))
                buttMer = Button(window, text = "", bg = "white", command = lambda: parse("", ""))
                buttTyn = Button(window, text = "", bg = "white", command = lambda: parse("", ""))

                labl.pack()
                buttMan.pack()
                buttLon.pack()
                buttNor.pack()
                buttWes.pack()
                buttMer.pack()
                buttTyn.pack()
                
                window.mainloop()

            def parse(derby1, derby2):
                pos1 = []
                pos2 = []
                total = 0
                total2 = 0
                with open("english premier league data.csv") as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    line_count = 0
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
                    print(derby1, "Average Possesion: ", avg)
                    print(derby2, "Average Possession", avg2)
                    print(f'Processed {line_count} lines.')

        main()
            
        
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
            def main():
                window = Tk()
                window.title("")
                window.geometry("250x250")
                window.configure(background = "black")
                labl = Label(window, text = "", fg = "white", bg = "black")
                buttEPL = Button(window, text = "", bg = "white", command = lambda: epl())

                labl.pack()
                buttEPL.pack()
                
                window.mainloop()
            def epl():
                window = Tk()
                window.title("EPL Data")
                window.geometry("300x300")
                window.configure(background = "black")
                labl = Label(window, text = "", fg = "white", bg = "black")
                buttMan = Button(window, text = "", bg = "white", command = lambda: parse("", ""))
                buttLon = Button(window, text = "", bg = "white", command = lambda: parse("", ""))
                buttNor = Button(window, text = "", bg = "white", command = lambda: parse("", ""))
                buttWes = Button(window, text = "", bg = "white", command = lambda: parse("", ""))
                buttMer = Button(window, text = "", bg = "white", command = lambda: parse("", ""))
                buttTyn = Button(window, text = "", bg = "white", command = lambda: parse("", ""))

                labl.pack()
                buttMan.pack()
                buttLon.pack()
                buttNor.pack()
                buttWes.pack()
                buttMer.pack()
                buttTyn.pack()
                
                window.mainloop()

            def parse(derby1, derby2):
                pos1 = []
                pos2 = []
                total = 0
                total2 = 0
                with open("english premier league data.csv") as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    line_count = 0
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
                    print(derby1, "Average Possesion: ", avg)
                    print(derby2, "Average Possession", avg2)
                    print(f'Processed {line_count} lines.')

        main()
            
        
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
