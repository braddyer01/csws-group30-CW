from tkinter import *
import csv

def main():
    window = Tk()
    window.title("Derbys and Rivalries Data")
    window.geometry("500x500")
    window.configure(background = "black")
    window.iconbitmap("favicon.ico")
    labl = Label(window, text = "Top 5 European Leagues", fg = "white", bg = "black")
    lablBlank = Label(window, text = "", fg = "white", bg = "black")
    buttEng = Button(window, text = "English Premier League", bg = "white", command = lambda: parse("English Premier League"))
    lablBlank2 = Label(window, text = "", fg = "white", bg = "black")
    buttFre = Button(window, text = "French Ligue 1", bg = "white", command = lambda: parse("French Ligue 1"))
    lablBlank3 = Label(window, text = "", fg = "white", bg = "black")
    buttSpa = Button(window, text = "Spanish La Liga", bg = "white", command = lambda: parse("Spanish La Liga"))
    lablBlank4 = Label(window, text = "", fg = "white", bg = "black")
    buttGer = Button(window, text = "German Bundesliga", bg = "white", command = lambda: parse("German Bundesliga"))
    buttIta = Button(window, text = "Italian Serie A", bg = "white", command = lambda: parse("Italian Serie A"))

    labl.pack()
    buttEng.pack()
    lablBlank.pack()
    buttFre.pack()
    lablBlank2.pack()
    buttSpa.pack()
    lablBlank3.pack()
    buttGer.pack()
    lablBlank4.pack()
    buttIta.pack()
    
    window.mainloop()

def parse(league):
    title = (league, "Data")
    window2 = Tk()
    window2.title(title)
    window2.geometry("500x500")
    window2.configure(background = "black")
    window2.iconbitmap("favicon.ico")
    scrollbar = Scrollbar(window2)
    scrollbar.pack(side = RIGHT, fill = Y)
    with open("english premier league data.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            while row[40] == year:
                text = (f'\t{row[1]} vs {row[2]} Score: {row[3]} Year: {row[40]}')
                labl = Label(window2, text = text, fg = "white", bg = "black").pack()
                line_count += 1
                break
        print(f'Processed {line_count} lines.')

    window2.mainloop()

main()

#print(f'\t{row[1]} vs {row[2]} Score: {row[3]} Year: {row[40]}')
