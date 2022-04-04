#Imports csv library
import csv
import matplotlib.pyplot as plt
plt.style.use('ggplot')

#Defines the subroutine csvimport
def csvimport():
    
    
    #Opens the csv file and creates a reader that puts the lines into a list variable
    with open('english premier league data1.csv', 'r') as csvfile:
        
        lines = csvfile.readlines()
        MANUTD = 0
        for line in lines:
            data = line.split(',')
            if (data[1]) == "MAN UTD":
                MANUTD = MANUTD + (data[36])


        
    
    #Prints list of csv cells
    print(MANUTD)


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
