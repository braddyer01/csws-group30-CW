#Imports csv library
import csv



#Defines the subroutine csvimport
def csvimport():
    
    
    #Opens the csv file and creates a reader that puts the lines into a list variable
    with open('english premier league data1.csv', 'r') as csvfile:
        
        lines = csvfile.readlines()
        homeTeam = []
        for line in lines:
            data = line.split(',')
            homeTeam.append(data[1])
        
    
    #Prints list of csv cells
    print(homeTeam)


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
