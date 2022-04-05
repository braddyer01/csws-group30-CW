import csv


premDataList = []
homeTeam = []
awayTeam = []
allTeams = []
ftScore = []
htScore = []

def readData():
    with open("english premier league data.csv") as custfile:
        rows = csv.reader(custfile, delimiter=',')
        lineNum=0
        for r in rows:
                homeTeam.append(r[1])
                awayTeam.append(r[2])
                ftScore.append(r[3])
                htScore.append(r[4])
                lineNum+=1

print(homeTeam[1])


def getHomeAwayTeam():
    index = 0
    for team in homeTeam:
        if team not in allTeams:
            print(team)
            allTeams.append(team)
            index+=1
    allTeams.remove('Home Team')

getHomeAwayTeam()
print(allTeams)