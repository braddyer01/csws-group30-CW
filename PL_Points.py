import matplotlib.pyplot as plt
import numpy as np
#importing the needed libraries 
   
Teams1 = ['Man City', 'Liverpool', 'Chelsea', 'Tottenham', 'Arsenal', 'Man United', 'Wolves', 'Everton', 'Leicester', 'West Ham', 'Watford', 'Crystal Palace', 'Newcastle', 'Bournemouth', 'Burnley', 'Southampton', 'Brighton', 'Cardiff City', 'Fulham', 'Huddersfield']
Points1 = [98, 97, 72, 71, 70, 66, 57, 54, 52, 52, 50, 49, 45, 45, 40, 39, 36, 34, 26, 16]

Teams2 = ['Liverpool', 'Man City', 'Man United', 'Chelsea', 'Leicester', 'Tottenham', 'Wolves', 'Arsenal', 'Sheffield', 'Burnley', 'Southampton', 'Everton', 'Newcastle', 'Crystal Palace', 'Brighton', 'West Ham', 'Aston Villa', 'Bournemouth', 'Watford', 'Norwich City']
Points2 = [99, 81, 66, 66, 62, 59, 59, 56, 54, 54, 52, 49, 44, 43, 41, 39, 35, 34, 34, 21]

Teams3 = ['Man City', 'Man United', 'Liverpool', 'Chelsea', 'Leicester', 'West Ham', 'Tottenham', 'Arsenal', 'Leeds', 'Everton', 'Aston Villa', 'Newcastle', 'Wolves', 'Crystal Palace', 'Southampton', 'Brighton', 'Burnley', 'Fulham', 'West Brom', 'Sheffield']
Points3 = [86, 74, 69, 67, 66, 65, 62, 61, 59, 59, 55, 45, 45, 44, 43, 41, 39, 28, 26, 23]
#Declaring all of the teams and the points that they recieved in that season

def menu():
    print("Please choose what season you would like to view:")
    print("[1] 2018/19")
    print("[2] 2019/20")
    print("[3] 2020/21")
    # Text based menu that allows the user to choose what season they would like to view


menu()
option1 = int(input("Please enter your option: "))

while option1 != 0:
    if option1 == 1:
        print("Premier League Table 2018/19")
        print("Please choose what type of data visualisation you would like to see:")
        print("[1] Bar Chart")
        print("[2] Pie Chart")
        print("[0] Exit the program.")
        # Text based menu thats allows the user to choose what type of visualisation they would like to view
      
        
        option2 = int(input("Please enter your option: "))

        while option2 != 0:
            if option2 == 1:
            # This option will display a visualisation of a bar chart
                plt.bar(Teams1, Points1)
                plt.title('Premier League Table 2018/19 Season')
                plt.xlabel('Teams')
                plt.ylabel('Points')
                plt.show()  
                plt.show(block=False)
                plt.close('all')                           
               
            elif option2 == 2:
            # This option will display a visualisation of a pie chart which displays the distribution of all points added up in the premier league table
                fig1 = plt.figure()
                ax1 = fig1.add_axes([0,0,1,1])
                ax1.axis('equal')
                ax1.pie(Points1, labels = Teams1,autopct='%.2f%%')
                plt.show()
            else:
                print("Invalid option, please try again.")

        print()    
        option2 = int(input("Please enter your option: "))
        plt.close(all)

    elif option1 == 2:
        
        print("Premier League Table 2019/20")
        print("Please choose what type of data visualisation you would like to see:")
        print("[1] Bar Chart")
        print("[2] Pie Chart")
        print("[0] Exit the program.")
        # Text based menu thats allows the user to input an option
      
        
        option3 = int(input("Please enter your option: "))

        while option3 != 0:
            if option3 == 1:
            # This option will display a visualisation of a bar chart
                plt.bar(Teams2, Points2)
                plt.title('Premier League Table 2019/20 Season')
                plt.xlabel('Teams')
                plt.ylabel('Points')
                plt.show()
               
            elif option3 == 2:
            # his option will display a visualisation of a pie chart which displays the distribution of all points in the premier league table
                fig2 = plt.figure()
                ax2 = fig2.add_axes([0,0,1,1])
                ax2.axis('equal')
                ax2.pie(Points2, labels = Teams2,autopct='%.2f%%')
                plt.show()
            else:
                print("Invalid option, please try again.")

        print()        
        option3 = int(input("Please enter your option: "))
    
    elif option1 == 3:
        print("Premier League Table 2020/21")
        print("Please choose what type of data visualisation you would like to see:")
        print("[1] Bar Chart")
        print("[2] Pie Chart")
        print("[0] Exit the program.")
        # Text based menu thats allows the user to input an option
      
        
        option4 = int(input("Please enter your option: "))

        while option4 != 0:
            if option4 == 1:
            # This option will display a visualisation of a bar chart
                plt.bar(Teams3, Points3)
                plt.title('Premier League Table 2020/21 Season')
                plt.xlabel('Teams')
                plt.ylabel('Points')
                plt.show()
               
            elif option4 == 2:
            # This option will display a visualisation of a pie chart which displays the distribution of all points in the premier league table
                fig3 = plt.figure()
                ax3 = fig3.add_axes([0,0,1,1])
                ax3.axis('equal')
                ax3.pie(Points3, labels = Teams3,autopct='%.2f%%')
                plt.show()
            else:
                print("Invalid option, please try again.")

        print()        
        option4 = int(input("Please enter your option: "))

    else:
        print("Invalid option, please try again.")
        # While loop if none of the requested input is given

    print()
    menu()
    option1 = int(input("Please enter your option: "))




print("Thank you, goodbye.")
plt.close('all')
# Closes any remaining figures open


