#---------- START OF JONAS' CODE (Number guessing game) ----------

from leaderboard import leaderboard #Defining some variables and functions that are crucial to this program's functioning
import random

def play_game(users, user_info): #Master function for the game part of the program.
	if not user_info and not user_info is 0: #Checks if the user is logged in and warns them about score saving.
		while True:
			match input("Your score will NOT BE SAVED if you do not log in. Type y to continue anyway. Type n to exit the game.: "):
				case "y":
					break
				case "n":
					return user_info
				case _:
					print("That's not a valid input. Try again.")

	num = random.randint(1, 100)
	score = 10
	while score != 0: #If the user hasn't lost yet
		while True:
			try:
				print(f"\nYou have {score} tries left.")
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
	
	if user_info or user_info == 0:
		if score == 0:
			print("Looks like you lost. Better luck next time!")
		else:
			print(f"Nice job! Your final score was: {score}")
			users[user_info]["scores"].append(score)
	else:
		print("You're not logged in, so your score won't be saved.")	
	
	leaderboard(users)
	return user_info

#---------- END OF JONAS' CODE (Number guessing game) ----------