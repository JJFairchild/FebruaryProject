#Jonas Fairchild, Avery Bowman, Yenesis Ravelo - High Score Tracker

#---------- START OF AVERY'S CODE (Main function, saving and retrieving scores) ----------

import random #Import the necessary modules and functions, and define the necessary variables.
import csv
import os

from game import play_game
from leaderboard import *
from users import login

users = []
user_info = False

with open("users.csv", "r") as file: #Read the file and make each line part of the dictionary
    csv_reader = csv.reader(file)
    for line in csv_reader:
        for value in line:
            if line.index(value) == 0:
                user = {"name": line[0], "scores": []}
            else:
                user["scores"].append(int(value))
        if user != "\n":
            users.append(user)

def main(users, user_info): #Main function that branches out to all parts of the program
    while True:
        os.system('cls')
        match input("What do you want to do?\n1. Log in\n2. Play game\n3. View Leaderboard\n4. Log out\n5. Exit\n"):
            case "1":
                users, user_info = login(users, user_info)
            case "2":
                user_info = play_game(users, user_info)
            case "3":
                leaderboard(users)
            case "4":
                user_info = False
                print("Successfully logged out.")
            case "5":
                break
            case _:
                print("That's not a valid input. Try again.")
        input("Done reading?: ")
    return users

users = main(users, user_info) #Call the main function

with open("users.csv", "w", newline="") as file: #Erase the contents of the file and write users to the file
    file.write("")
    csv_writer = csv.writer(file)
    for user in users:
        row = [user["name"]]
        for score in user["scores"]:
            row.append(score)
        csv_writer.writerow(row)

#---------- END OF AVERY'S CODE (Main function, saving and retrieving scores) ----------