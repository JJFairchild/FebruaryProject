#---------- START OF YENESIS' CODE (User profiles) ----------

def login(users, user_info):
    while True:
        match input("Do you want to log in or create an account?: ").lower():
            case "log in":
                for user in users:
                    print(f"- {user["name"]}")
                while True:
                    username = input("Who do you want to log in as?: ")
                    for user in users:
                        if user["name"] == username:
                            print("Successfully logged in.")
                            user_info = users.index(user)
                            return users, user_info
                    print("That's not a user. Try again.")
            case "create an account":
                name = input("What do you want to name your account?: ")
                users.append({"name": name, "scores": []})
                user_info = users.index({"name": name, "scores": []})
                print("You are now logged in.")
                return users, user_info
            case _:
                print("That's not a valid input. Options: 'log in', 'create an account'")

print(login([{"name": "EpixGD", "scores": [2, 3, 5]}], False))

#---------- END OF YENESIS' CODE (User profiles) ----------