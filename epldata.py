from ast import increment_lineno
import csv
import matplotlib.pyplot as plt

plt.style.use('ggplot')

file = open("english premier league data.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
#print(rows)
file.close()



x = ['Man City', 'Liverpool', 'Chelsea', 'Tottenham', 'Arsenal', 'Man Utd',]
energy = [98,97,72,71,70,66]

x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos,energy,color = 'green')
plt.xlabel("Points Earned")
plt.ylabel("Teams")
plt.title("Points earned by EPL teams (2018-19)")

plt.xticks(x_pos,x)
#plt.show()
