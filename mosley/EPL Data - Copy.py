from tkinter import *
import csv

def main():
    window = Tk()
    window.title("EPL Data")
    window.geometry("225x150")
    window.configure(background = "black")
    window.iconbitmap("favicon.ico")
    labl = Label(window, text = "English Premier League", fg = "white", bg = "black")
    butt2014 = Button(window, text = "Manchester Derby", bg = "white", command = lambda: parse("MAN UTD", "MAN CITY"))
    butt2015 = Button(window, text = "2015", bg = "white", command = lambda: parse("2015"))
    butt2016 = Button(window, text = "2016", bg = "white", command = lambda: parse("2016"))
    butt2017 = Button(window, text = "2017", bg = "white", command = lambda: parse("2017"))

    labl.pack()
    butt2014.pack()
    butt2015.pack()
    butt2016.pack()
    butt2017.pack()
    
    window.mainloop()

def parse(derby1, derby2):
    with open("english premier league data.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            while (row[1] == derby1 or row[1] == derby2) and (row[2] == derby1 or row[2] == derby2):
                print(f'\t{row[1]} vs {row[2]} Score: {row[3]} Year: {row[40]}')
                line_count += 1
                break
        print(f'Processed {line_count} lines.')

main()

#print(f'\t{row[1]} vs {row[2]} Score: {row[3]} Year: {row[40]}')


