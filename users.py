#---------- START OF YENESIS' CODE (User profiles) ----------

class UserProfileManager:
    def __init__(self):
        self.profiles = {}
        self.current_user = None

    def create_profile(self):
        username = input("Enter a username: ")
        if username in self.profiles:
            print("Username already exists.")
        else:
            self.profiles[username] = {}
            print(f"Profile created for {username}.")

    def sign_in(self):
        username = input("Enter your username to sign in: ")
        if username in self.profiles:
            self.current_user = username
            print(f"{username} signed in.")
        else:
            print("Profile not found. Please create a profile first.")

    def view_profile(self):
        username = input("Enter the username to view profile: ")
        if username in self.profiles:
            print(f"Profile for {username}: {self.profiles[username]}")
        else:
            print("Profile not found.")

# Example interactive usage
manager = UserProfileManager()
while True:
    action = input("Choose an action: create, sign in, sign out, view, or exit: ").strip().lower()
    if action == "create":
        manager.create_profile()
    elif action == "sign in":
        manager.sign_in()
    elif action == "view":
        manager.view_profile()
    elif action == "exit":
        break
    else:
        print("Invalid action. Please try again.")


def login(users):
    for user in users:
        print(f"- {user["name"]}")
    while True:
        username = input("Who do you want to log in as?: ")
        for user in users:
            if user["name"] == username:
                print("Successfully logged in.")
                return users.index(user)
        print("That's not a user. Try again.")

#---------- END OF YENESIS' CODE (User profiles) ----------