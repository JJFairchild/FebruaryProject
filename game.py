#---------- START OF JONAS' CODE (Number guessing game) ----------

from leaderboard import leaderboard #Defining some variables and functions that are crucial to this program's functioning
import random
users = [{"name": "Jonas", "scores": []}] 
user_info = users[0]

def play_game(): #Master function for the game part of the program.
	num = random.randint(1, 100)
	score = 10
	while score != 0: #If the user hasn't lost yet
		while True:
			try:
				print(f"You have {score} tries left.")
				guess = int(input("What is your guess?: ")) #Get the user's guess
				break
			except:
				print("That's not a valid input. Try again.")
		if guess == num: #Tell the user if their guess is too small or large.
			break
		elif guess < num:
			print("Your guess was too small.")
			score -= 1
		elif guess > num:
			print("Your guess was too large.")
			score -= 1
	
	if user_info:
		if score == 0:
			print("Looks like you lost. Better luck next time!")
		else:
			print(f"Nice job! Your final score was: {score}")
			user_info["scores"].append(score)
	else:
		print("You're not logged in, so your score won't be saved.")	
	
	leaderboard()
	return user_info

#---------- END OF JONAS' CODE (Number guessing game) ----------