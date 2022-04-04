#imports for graph plotting and stuff
from tkinter import *
import csv
import matplotlib.pyplot as plt
import numpy as np

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



