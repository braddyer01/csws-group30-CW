import matplotlib.pyplot as plt
   
Teams = ['Liverpool', 'Man City', 'Man United', 'Chelsea', 'Leicester', 'Tottenham', 'Wolves', 'Arsenal', 'Sheffield', 'Burnley', 'Southampton', 'Everton', 'Newcastle', 'Crystal Palace', 'Brighton', 'West Ham', 'Aston Villa', 'Bournemouth', 'Watford', 'Norwich City']
Points = [99, 81, 66, 66, 62, 59, 59, 56, 54, 54, 52, 49, 44, 43, 41, 39, 35, 34, 34, 21]

plt.bar(Teams, Points)
plt.title('Premier League Table 2019/20 Season')
plt.xlabel('Teams')
plt.ylabel('Points')
plt.show()