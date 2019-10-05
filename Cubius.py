# Marcus Cornes


# This will allow me to use date and time in my program
import datetime

# This python module allows me to have OS priviliges that I can use to delete files
import os

# This module will allow me to open URL's from your web browser
import webbrowser

# This is the start message
print("Welcome to Cubius made by Marcus Cornes!")

# This code will run the program forever!
while True:

    # This makes a prompt to enter a command
    response = input("Enter a command: ")


    # This is the trigger that will print the current version of my OS
    if response == "version":
        print("Cubius 0.0.1")


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

    
    if response == "exit":
        break