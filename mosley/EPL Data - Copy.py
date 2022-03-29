from tkinter import *
import csv
import matplotlib.pyplot as plt
import numpy as np

def choice(derby1, derby2):
    window = Tk()
    window.title("English Premier League")
    window.geometry("250x250")
    window.configure(background = "black")
    window.iconbitmap("favicon.ico")
    labl = Label(window, text = "Visualisation Choices", fg = "white", bg = "black")
    buttEPL = Button(window, text = "Possession", bg = "white", command = lambda: parse(derby1, derby2, "Possession"))
    buttFL = Button(window, text = "Goals", bg = "white", command = lambda: parse(derby1, derby2, "Goals"))

    labl.pack()
    buttEPL.pack()
    buttFL.pack()
    
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
    total = 0
    total2 = 0
   
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

main()



