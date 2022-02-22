#imports---------------------------------------------------------------------------------------------------------
from tkinter import *
#page one--------------------------------------------------------------------------------------------------------
def page_one():
    key = 0
    print ("""-------------------PAGE1-------------------""")
    while key == 0:
        choice = input("""Please choose a page option: """)
        if choice == "0":
            key = 1
            menu()
        else:
            print ("Invalid input")
#page two-------------------------------------------------------------------------------------------------------
def page_two():
    import csv
    key = 0

    with open('Book.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
        print ("""-------------------PAGE2-------------------
    1) Parce Data
    0) EXIT
    """)
    while key == 0:
        choice = input("""Please choose a page option: """)
        if choice == "0":
            key = 1
            menu()
        elif choice == "1":
            print(data)
            
        
        else:
            print ("Invalid input")
#page three------------------------------------------------------------------------------------------------------
def page_three():
    key = 0
    print("""-------------------PAGE3-------------------
1)Visual Representation
2)Written Representation
0)EXIT
""")
    while key == 0:
        choice = input("""Please choose a page option: """)
        if choice == "0":
            key = 1
            menu()
        elif choice == "1":
            print("Diagram has opened")
            window = Tk()
            window.title("test")
            window.geometry("250x250")
            window.mainloop()
        elif choice == "2":
            print("Text based data")
        
        else:
            print ("Invalid input")
    

#main menu-------------------------------------------------------------------------------------------------------    
def menu():
    print ("""-------------------MENU-------------------
    1) Page Test
    2) Csv Test
    3) Tkinter Test
    4) ...
    5) ...
    6) ...
    0) EXIT
    """)
    main_choice()
def main_choice():   
    choose = input("Please choose a menu option: ")
    if choose == "1":
        print ("001")
        page_one()
    elif choose == "2":
        print ("010")
        page_two()
    elif choose == "3":
        print ("011")
        page_three()
    elif choose == "4":
        print ("100")
        page_one()
    elif choose == "5":
        print ("101")
        page_two()
    elif choose == "6":
        print ("110")
    elif choose == "0":
        exit()
    else:
        print ("error")
        main_choice()

menu()
