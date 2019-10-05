# Marcus Cornes, Cube Inc.
# GNU License


# This will allow me to use date and time in my program
import datetime

# This python module allows me to have OS priviliges that I can use to delete files
import os

# This module will allow me to open URL's from your web browser
import webbrowser

# This is the start message
print("Welcome to CubiusOS made by Marcus Cornes!")

# This code will run the program forever!
while True:

    # This makes a prompt to enter a command
    response = input("Enter a command: ")


    # This is the trigger that will print the current version of my OS
    if response == "version":
        print("CubiusOS 0.0.1")


    # This is the trigger that will print the date and time using the datetime python module
    if response == "time":
        try:
            x = datetime.datetime.now()
            print(x)
        except:
            print("The time program is not working.")
            print("Please report this error at the errors page on GitHub :(")


    # This is the trigger that will create a new .txt file
    if response == "txt":
        try:
            f = open(".txt", "x")
            f.close
            print("Created .txt file in the current folder.")
        except FileExistsError:
            print("I'm sorry but it looks like you already have a filecalled .txt!")
            delete = input("Do you want me to delete it and make a new .txt file? Y/N ")

            if delete == "Y":
                os.remove(".txt")
                f = open(".txt", "x")
                f.close
                print("Process ran successfully ;)")


            if delete == "N":
                pass


    # This is a trigger that will run the code and the code will remove the current directory
    if response == "rmDir":
        folder = input("What is the name of the folder you want to delete? ")

        try:
            os.rmdir(folder)
            print("Operation successful!")
        except FileNotFoundError:
            print("Sorry, the folder you specified couldn't be found! Make sure you spelt the folder name correctly or try again!")
            print("If problems keep persisting, please visit the github repo and report an issue there.")
        

    # This trigger will be able to open websites via your web browser
    if response == "url":
        web = input("What URL do you want to go to? ")
        webbrowser.open(web)
        print("Sorry but the URL you typed in couldn't be found! Maybe you should try typing the full URL.")