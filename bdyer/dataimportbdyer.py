import csv

premDataList = []
homeTeam = []
awayTeam = []
ftScore = []
htScore = []

with open("english premier league data.csv") as custfile:
    rows = csv.reader(custfile, delimiter=',')
    for r in rows:
        premDataList.append(r)


print(premDataList[4])