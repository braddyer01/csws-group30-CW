#Imports csv library
import csv
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *


#Defines the subroutine csvimport
def csvimport():
    
    
    
    #Opens the csv file and creates a reader that puts the lines into a list variable
    with open('english premier league data.csv', 'r') as csvfile:
        
        lines = csvfile.readlines()
        goals = []
        titles = [20,6,7,13,19,2,1,9,7,0,0,4,3,0,0,0,3,0,2,0]
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

            if (data[2]) == "MAN UTD":
                MANUTD = MANUTD + int(data[37])
            elif (data[2]) == "CHELSEA":
                CHEAL = CHEAL + int(data[37])
               
            elif (data[2]) == "MAN CITY":
                MANCIT = MANCIT + int(data[37])
                
            elif (data[2]) == "ARSENAL":
                ARSENAL = ARSENAL + int(data[37])
                
            elif (data[2]) == "LIVERPOOL":
                LIVERPOOL = LIVERPOOL + int(data[37])
                
            elif (data[2]) == "TOTTENHAM":
                 SPURS = SPURS + int(data[37])
                
            elif (data[2]) == "LEICESTER CITY":
                LEISTER = LEISTER + int(data[37])
               
            elif (data[2]) == "EVERTON":
                EVERTON = EVERTON + int(data[37])
                
            elif (data[2]) == "ASTON VILLA":
                VILLA = VILLA + int(data[37])
                
            elif (data[2]) == "SOUTHAMPTON":
                SOUTHHAMPT = SOUTHHAMPT + int(data[37])
                
            elif (data[2]) == "WEST HAM":
                WESTHAM = WESTHAM + int(data[37])
                
            elif (data[2]) == "NEWCASTLE":
                NEWCASTLE = NEWCASTLE + int(data[37])
                
            elif (data[2]) == "WOLVES":
                WOLVES = WOLVES + int(data[37])
                
            elif (data[2]) == "WATFORD":
                WATFORD = WATFORD + int(data[37])
               
            elif (data[2]) == "CRYSTAL PALACE":
                CRYSTAL = CRYSTAL + int(data[37])
               
            elif (data[2]) == "NORWICH":
                NORWICH = NORWICH + int(data[37])
              
            elif (data[2]) == "LEEDS UTD":
                LEEDS = LEEDS + int(data[37])
                
            elif (data[2]) == "BRIGHTON":
                BRIGHTON = BRIGHTON + int(data[37])
                
            elif (data[2]) == "BURNLEY":
                BURNLEY = BURNLEY + int(data[37])
                
            elif (data[2]) == "WEST BROM":
                WESTBROM = WESTBROM + int(data[37])
                

    


        
    goals.append(MANUTD)
    goals.append(CHEAL)
    goals.append(MANCIT)
    goals.append(ARSENAL)
    goals.append(LIVERPOOL)
    goals.append(SPURS)
    goals.append(LEISTER)
    goals.append(EVERTON)
    goals.append(VILLA)
    goals.append(SOUTHHAMPT)
    goals.append(WESTHAM)
    goals.append(NEWCASTLE)
    goals.append(WOLVES)
    goals.append(WATFORD)
    goals.append(CRYSTAL)
    goals.append(NORWICH)
    goals.append(LEEDS)
    goals.append(BRIGHTON)
    goals.append(BURNLEY)
    goals.append(WESTBROM)

    #Prints list of csv cells
    
    
    x = np.arange(20)
    y1 = goals
    y2 = titles
    width = 0.4
        
        
    plt.bar(x-0.2, y1, width)
    plt.bar(x+0.2, y2, width)
    plt.xticks(x, ['MAN UTD', 'CHELSEA', 'MAN CITY', 'ARSENAL', 'LPOOL', 'SPURS', 'LEICESTER', 'EVERTON', 'ASTON VILLA', 'SOUTHAMPTON', 'WEST HAM', 'NEWCASTLE', 'WOLVES', 'WATFORD', 'CRYSTAL PALACE', 'NORWICH', 'LEEDS', 'BRIGHTON', 'BURNLEY', 'BRENTFORD'])
    plt.xlabel("Teams (In order of popularity)")
    plt.ylabel("Goals Scored (Blue) Titles Won (Orange)")

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
