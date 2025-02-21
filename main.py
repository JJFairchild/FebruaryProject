#Jonas Fairchild, Avery Bowman, Yenesis Ravelo - High Score Tracker

import random
import csv
import os

#---------- START OF AVERY'S CODE (Retrieve user info) ----------



#---------- END OF AVERY'S CODE (Retrieve user info) ----------

#---------- START OF YENESIS' CODE (User profiles) ----------



#---------- END OF YENESIS' CODE (User profiles) ----------

#---------- START OF AVERY'S CODE (Leaderboard) ----------



#---------- END OF AVERY'S CODE (Leaderboard) ----------

#---------- START OF JONAS' CODE (Number guessing game) ----------

#Assume that users is a list of dictionaries, each containing a name (user[“name”]) and a list of scores (user[“scores”]).
#Assume that user_info is the user in users that is currently logged in.
#display_leaderboard() is a function that displays the entire leaderboard.
#These values are not defined in this part of the program.

def play_game():
	num = random.randint(1, 100)
	score = 10
	while score != 0:
		while True:
			try:
				guess = int(input("What is your guess?: "))
				break
			except:
				print("That's not a valid input. Try again.")
		if guess == num:
			break
		elif guess < num:
			print("Your guess was too small.")
			score -= 1
		elif guess > num:
			print("Your guess was too large.")
			score -= 1
	if user_info:
		if score == 0:
			print("Whoops! You lost.")
		else:
			print(f"Nice job! Your final score was: {score}")
			user_info["scores"].append(score)
		return user_info
			
			
    
    if user_info:
        if score == 0:
		    Tell user they lost
		    Return user_info
	    ELSE:
		    Congratulate user
		    Add score to user_info
		Return user info
	ELSE:
		Tell the user that their score wasn’t saved, since they aren’t logged in.
	
display_leaderboard()
    
    
    

#play_game is called in the main function.


#---------- END OF JONAS' CODE (Number guessing game) ----------

#---------- START OF AVERY'S CODE (Main function and saving scores) ----------



#---------- END OF AVERY'S CODE (Main function and saving scores) ----------