from sys import displayhook
from tkinter import *
import csv
from turtle import ht
import matplotlib.pyplot as plt
import numpy as np

premDataList = []
homeTeam = []
awayTeam = []
allTeams = []
ftScore = []
htScore = []
ftScoreHome = []
ftScoreAway = []
htScoreAway = []
htScoreHome = []
homeHTGoals = []
homeFTGoals = []
awayHTGoals = []
awayFTGoals = []
averageFTHGoals = 0
averageHTAGoals = 0
averageFTAGoals = 0
averageHTHGoals = 0

#Variables declared

def ok():
    print("You have chosen "+dropdownVariable.get())
    chosenTeam = dropdownVariable.get()
    getHTGoals(chosenTeam)
    getFTGoals(chosenTeam)
    displayData(chosenTeam)
    

def getHomeAwayTeam():
    index = 0
    for team in homeTeam:
        if team not in allTeams:
            print(team)
            allTeams.append(team)
            index+=1
    allTeams.remove('Home Team')
    return allTeams

def readData():
    with open("english premier league data.csv") as custfile:
        rows = csv.reader(custfile, delimiter=',')
        for r in rows:
                homeTeam.append(r[1])
                awayTeam.append(r[2])
                premDataList.append(r)
                

def getHTGoals(chosenTeam):
    for games in premDataList:
        if games[1] == chosenTeam:
            htScoreHome.append(games[4])
        elif games[2] == chosenTeam:
            htScoreAway.append(games[4])
        
        

def getFTGoals(chosenTeam):
    for games in premDataList:
        if games[1] == chosenTeam:
            ftScoreHome.append(games[3])
        elif games[2] == chosenTeam:
            ftScoreAway.append(games[3])


def displayData(chosenTeam):
    counter = 0
    for scores in ftScoreHome:
        x = scores.split("-")
        homeFTGoals.append(x[0])
        counter += int(x[0])
    averageFTHGoals = counter / len(homeFTGoals)
        
    counter = 0
    for scores in htScoreHome:
        x = scores.split("-")
        homeHTGoals.append(x[0])
        counter += int(x[0])
    averageHTHGoals = counter / len(homeHTGoals)

    counter = 0
    for scores in ftScoreAway:
        x = scores.split("-")
        awayFTGoals.append(x[1])
        counter += int(x[1])
    averageFTAGoals = counter / len(awayFTGoals)

    counter = 0
    for scores in htScoreAway:
        x = scores.split("-")
        awayHTGoals.append(x[1])
        counter += int(x[1])
    averageHTAGoals = counter / len(awayHTGoals)

    displayWindow = Tk()
    displayWindow.title("Half Time vs Full Time")
    displayWindow.geometry("400x400")
    displayWindow.configure(background="black")
    chosenTeamLab = Label(displayWindow, text = "Chosen Team ="+chosenTeam, fg="white",bg="black")
    HomeScoreHTLabel = Label(displayWindow, text= "Home average goals at Half Time: "+str(averageHTHGoals), fg = "white", bg = "black")
    HomeScoreFTLabel = Label(displayWindow, text= "Home average goals at Full Time: "+str(averageFTHGoals), fg = "white", bg = "black")
    AwayScoreHTLabel = Label(displayWindow, text= "Away average goals at Half Time: "+str(averageHTAGoals), fg = "white", bg = "black")
    AwayScoreFTLabel = Label(displayWindow, text= "Away average goals at Full Time: "+str(averageFTAGoals), fg = "white", bg = "black")
    chosenTeamLab.pack()
    AwayScoreFTLabel.pack()
    AwayScoreHTLabel.pack()
    HomeScoreFTLabel.pack()
    HomeScoreHTLabel.pack()

    plt.rcParams['font.size'] = '6'
    plt.bar([chosenTeam +" Average HT Goals", chosenTeam+" Average FT Goals", "League Average HT Goals", "League Average FT Goals"],[(averageHTHGoals+averageHTAGoals)/2,(averageFTAGoals+averageFTHGoals/2),0.5,0.98])
    plt.show()




    

        

readData()
        
        




getHomeAwayTeam()
mainWindow = Tk()
topFrame = Frame(mainWindow)
topFrame.pack()
frameTwo = Frame(mainWindow)
frameTwo.pack()
mainWindow.title("Half Time vs Full Time")
mainWindow.geometry("400x400")
mainWindow.configure(background="black")
team1Lab = Label(topFrame, text = "Select team: ", fg = "white", bg = "black")
dropdownVariable = StringVar(mainWindow)
dropdownVariable.set(allTeams[0])
dropdown1 = OptionMenu(mainWindow, dropdownVariable, *allTeams)
dropdown1.pack()
button = Button(mainWindow, text="OK", command=ok)
button.pack()
team1Lab.pack(side = "left")



mainWindow.mainloop()


