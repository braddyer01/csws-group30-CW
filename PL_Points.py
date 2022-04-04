import matplotlib.pyplot as plt
import numpy as np
   
Teams = ['Liverpool', 'Man City', 'Man United', 'Chelsea', 'Leicester', 'Tottenham', 'Wolves', 'Arsenal', 'Sheffield', 'Burnley', 'Southampton', 'Everton', 'Newcastle', 'Crystal Palace', 'Brighton', 'West Ham', 'Aston Villa', 'Bournemouth', 'Watford', 'Norwich City']
Points = [99, 81, 66, 66, 62, 59, 59, 56, 54, 54, 52, 49, 44, 43, 41, 39, 35, 34, 34, 21]

def menu():
    print("Premier League Table 2019/20")
    print("Please choose what type of data visualisation you would like to see:")
    print("[1] Bar Chart")
    print("[2] Pie Chart")
    print("[0] Exit the program.")

menu()
option = int(input("Please enter your option: "))

while option != 0:
    if option == 1:
        #This option will display a visualisation of a bar chart
        plt.bar(Teams, Points)
        plt.title('Premier League Table 2019/20 Season')
        plt.xlabel('Teams')
        plt.ylabel('Points')
        plt.show()
    elif option == 2:
        #This option will display a visualisation of a pie chart
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        ax.axis('equal')
        ax.pie(Points, labels = Teams,autopct='%.2f%%')
        plt.show()
    else:
        print("Invalid option, please try again.")

    print()
    menu()
    option = int(input("Please enter your option: "))

print("Thank you, goodbye.")



