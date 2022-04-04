#Imports csv library
import csv
from http.client import BAD_REQUEST
import matplotlib.pyplot as plt
from sqlalchemy import Integer
plt.style.use('ggplot')

#Defines the subroutine csvimport
def csvimport():
    
    
    #Opens the csv file and creates a reader that puts the lines into a list variable
    with open('english premier league data.csv', 'r') as csvfile:
        
        lines = csvfile.readlines()
        goals = 0
        MANUTD = 0
        CHEAL = 0
        MANCIT = 0
        ARSENAL = 0
        LIVERPOOL = 0
        SPURS = 0
        LEISTER = 0
        EVERTON = 0
        VILLA = 0
        SOUTHHAMPT = 0
        WESTHAM = 0
        NEWCASTLE = 0
        WOLVES = 0
        WATFORD = 0
        CRYSTAL = 0
        NORWICH = 0
        LEEDS = 0
        BRIGHTON = 0
        BURNLEY = 0
        WESTBROM = 0
        


        for line in lines:
            data = line.split(',')
            if (data[1]) == "MAN UTD":
                MANUTD = MANUTD + int(data[36])
            elif (data[1]) == "CHELSEA":
                CHEAL = CHEAL + int(data[36])
               
            elif (data[1]) == "MAN CITY":
                MANCIT = MANCIT + int(data[36])
                
            elif (data[1]) == "ARSENAL":
                ARSENAL = ARSENAL + int(data[36])
                
            elif (data[1]) == "LIVERPOOL":
                LIVERPOOL = LIVERPOOL + int(data[36])
                
            elif (data[1]) == "TOTTENHAM":
                 SPURS = SPURS + int(data[36])
                
            elif (data[1]) == "LEICESTER CITY":
                LEISTER = LEISTER + int(data[36])
               
            elif (data[1]) == "EVERTON":
                EVERTON = EVERTON + int(data[36])
                
            elif (data[1]) == "ASTON VILLA":
                VILLA = VILLA + int(data[36])
                
            elif (data[1]) == "SOUTHHAMPTON":
                SOUTHHAMPT = SOUTHHAMPT + int(data[36])
                
            elif (data[1]) == "WEST HAM":
                WESTHAM = WESTHAM + int(data[36])
                
            elif (data[1]) == "NEWCASTLE":
                NEWCASTLE = NEWCASTLE + int(data[36])
                
            elif (data[1]) == "WOLVES":
                WOLVES = WOLVES + int(data[36])
                
            elif (data[1]) == "WATFORD":
                WATFORD = WATFORD + int(data[36])
               
            elif (data[1]) == "CRYSTAL PALACE":
                CRYSTAL = CRYSTAL + int(data[36])
               
            elif (data[1]) == "NORWICH":
                NORWICH = NORWICH + int(data[36])
              
            elif (data[1]) == "LEEDS UTD":
                LEEDS = LEEDS + int(data[36])
                
            elif (data[1]) == "BRIGHTON":
                BRIGHTON = BRIGHTON + int(data[36])
                
            elif (data[1]) == "BURNLEY":
                BURNLEY = BURNLEY + int(data[36])
                
            elif (data[1]) == "WEST BROM":
                WESTBROM = WESTBROM + int(data[36])
                

    


        
    
    #Prints list of csv cells
    print(goals)


def matplot():

    x = ['Man Utd', 'West Ham Utd', 'Chealsea', 'Manchester City', 'Liverpool']
    energy = [48, 49, 57, 68, 75]

    x_pos = [i for i, _ in enumerate(x)]

    plt.bar(x_pos, energy, color='green')
    plt.xlabel("Team")
    plt.ylabel("Goals scored")
    plt.title("Goals scored by top teams")

    plt.xticks(x_pos, x)

    plt.show()

#Defines the subroutine main
def main():

    #Creates a loop for the main menu
    loop = "0"
    while loop == "0":

        #Accepts user input to choose from the menu options - Uses numbers so capitals dont matter - Could also use .Upper() function
        userChoice = input("------Menu------\n\n1. Read csv file\n\n2. Exit\n\n")
        if userChoice == "1":
            csvimport()
            print("\n\nSelect another option: \n")
        elif userChoice == "2":
            print("Quitting...")
            loop = "1"
        else:
            print("\n\nInvalid input! Try again: \n\n")


#Calls the main menu subroutine 
main()
