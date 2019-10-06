# Marcus Cornes


# This will allow me to use date and time in my program
import datetime

# This python module allows me to have OS priviliges that I can use to delete files
import os

# This module will allow me to open URL's from your web browser
import webbrowser


# This is the start message
print("Hello!")

# This code will run the program forever!
while True:

    # This makes a prompt to enter a command
    response = input("Enter a command: ")


    # This is the trigger that will print the current version of my OS
    if response == "version":
        print("Cubius 0.0.1")
        print(os.uname())


    # This is the trigger that will print the date and time using the datetime python module
    if response == "time":
        try:
            x = datetime.datetime.now()
            print("")
            print(x)
            print("")
        except:
            print("")
            print("The time program is not working.")
            print("")
            print("Please report this error at the errors page on GitHub :(")
            print("")


    # This is the trigger that will create a new .txt file
    if response == "txt":
        try:
            f = open(".txt", "x")
            f.close
            print("")
            print("Created .txt file in the current folder.")
            print("")
        except FileExistsError:
            print("")
            print("I'm sorry but it looks like you already have a filecalled .txt!")
            print("")
            delete = input("Do you want me to delete it and make a new .txt file? Y/N ")

            if delete == "Y":
                os.remove(".txt")
                f = open(".txt", "x")
                f.close
                print("")
                print("Process ran successfully ;)")
                print("")


            if delete == "N":
                print("")


    # This is a trigger that will run the code and the code will remove the current directory
    if response == "rmDir":
        print("")
        folder = input("What is the name of the folder you want to delete? ")

        try:
            os.rmdir(folder)
            print("")
            print("Operation successful!")
            print("")
        except FileNotFoundError:
            print("")
            print("Sorry, the folder you specified couldn't be found! Make sure you spelt the folder name correctly or try again!")
            print("")
            print("If problems keep persisting, please visit the github repo and report an issue there.")
            print("")
        

    # This trigger will be able to open websites via your web browser
    if response == "url":
        print("")
        web = input("What URL do you want to go to? ")
        try:
            webbrowser.open(web)
        except:
            print("")
            print("Sorry but the URL you typed in couldn't be found! Maybe you should try typing the full URL.")
            print("")


   # This trigger will give you help when the user types in "help"
    if response == "help":
        print("")
        print("version - Will get you the current version number you are using of cubius.")
        print("")
        print("time - Will get you the current time.")
        print("")
        print("txt - Will create a .txt file in the current directory.")
        print("")
        print("rmDir - Will remove the directory / folder you specify.")
        print("")
        print("url - Will open the URL that you specify in your preferred web browser.")
        print("")
        print("help - Will bring you a list of commands that you can use in cubius and will tell you what they do.")
        print("")
        print("calculator - Will bring up a simple and easy to use calculator.")
        print("")
        print("rmFile - Will remove a file.")
        print("")
        print("rename - Will allow you to rename a file.")
        print("")
        print("MakeDir - Will make a directory / folder.")
        print("")
        print("WorkingDir - Will print the working directory / folder.")
        print("")
        print("open - Will print out the contents of a file.")
        print("")
        print("caterpillar - Will play the caterpillar game.")
        print("")
        print("MatchMaker - Will play the match maker game")

    
    # This bit of code will exit the loop.
    if response == "exit":
        break


    if response == "calculator":
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if (choice>=1 and choice<=4):
            print("Enter two numbers: ")
            num1 = int(input())
            num2 = int(input())
            if choice == 1:
    	        res = num1 + num2
    	        print("Result = ", res)
            elif choice == 2:
    	        res = num1 - num2
    	        print("Result = ", res)
            elif choice == 3:
    	        res = num1 * num2
    	        print("Result = ", res)
            elif choice == 4:
    	        res = num1 / num2
    	        print("Result = ", res)
            else:
                print("Wrong input..!!")


    if response == "caterpillar":
        import caterpillargame


    if response == "rmFile":
        print("")
        fileName = input("What is the name of the file you want to delete?")
        try:
            os.remove(fileName)
            print("")
            print("Operation successful!")
            print("")
        except:
            print("")
            print("Sorry but the file couldn't be located.")
            print("")


    
    if response == "rename":
        name = input("What is the current name of the file / folder you want to rename? ")
        name2 = input("What is the new name of the file / folder you want to rename? ")
        try:
            os.rename(name, name2)
            print("Operation successful!")
        except:
            print("Sorry, but it looks like the operation failed! Make sure you spelt everything correctly and try again.")


    
    if response == "MakeDir":
        folder = input("What is the name of the new folder?")
        try:
            os.mkdir(folder)
            print("Operation successful!")
        except:
            print("Sorry, the folder already exists!")



    if response == "WorkingDir":
        try:
            print("")
            print(os.getcwd())
            print("")
        except:
            print("Sorry, we failed to get the current working directory!")


    if response == "open":
        doc = input("What is the name of the file you would like to read?")
        try:
            f = open(doc, "r")
            print(f.read())
            print("")
        except:
            print("Sorry, but the file you specified could not be found!")


    if response == "MatchMaker":
        import Matchmaker



    if response == "lives":
        import NineLives