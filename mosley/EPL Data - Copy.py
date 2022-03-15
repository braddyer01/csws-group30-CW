from tkinter import *
import csv

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

#print(f'\t{row[1]} vs {row[2]} Score: {row[3]} Year: {row[40]}')

#8 9


