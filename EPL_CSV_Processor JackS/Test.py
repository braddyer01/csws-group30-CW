import csv
data = []
print ("First page")
##x = 0
##while x < 1:
print ("Please choose one of the following options")
choice = input ("""
A) View Data
B) ---
C) ---
D) EXIT

""")

##def parse(year):
       ## with open("english premier league data.csv") as csv_file:
           ## csv_reader = csv.reader(csv_file, delimiter=',')
           ## line_count = 0
          ## for row in csv_reader:
             ##   while row[40] == year:
               ##     print(f'\t{row[1]} vs {row[2]} Home Team rating: {row[6]} Away Team rating: {row[7]} Match Excitement: {row[5]}')
               ##     line_count += 1
                ##    break
                ##print(f'Processed {line_count} lines.')

if choice == "A":
    year = input ("Please choose a year 2014-2017")
    team = input ("Please choose a team")
    ##parse(year)
    with open("english premier league data.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
            
    col = [x[1] for x in data]
    print (col)
    if team in col:
        for x in range(0,len(data)):
            if team == data[x][1]:
                print(data[x])
    

