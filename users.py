#---------- START OF YENESIS' CODE (User profiles) ----------

def login(users, user_info): #Function that handles logging in
    while True: 
        match input("Do you want to log in or create an account?: ").lower(): #User chooses whether to log in or create an account
            case "log in":
                for user in users: #Display the users to sign in as
                    print(f'- {user["name"]}')
                while True:
                    username = input("Who do you want to log in as?: ") #Ask the user who they want to sign in as
                    for user in users:
                        if user["name"] == username: #If their choice is valid, set user_info to that choice
                            print("Successfully logged in.")
                            user_info = users.index(user)
                            return users, user_info
                    print("That's not a user. Try again.")
            case "create an account":
                name = input("What do you want to name your account?: ")
                users.append({"name": name, "scores": []}) #Creates an account
                user_info = users.index({"name": name, "scores": []}) #Automatically logs the user in as the account they just created
                print("You are now logged in.")
                return users, user_info
            case _:
                print("That's not a valid input. Options: 'log in', 'create an account'")

#---------- END OF YENESIS' CODE (User profiles) ----------