#---------- START OF AVERY'S CODE (Leaderboard) ----------

# Import the high score tracker module

import copy


def spec_sort(i):
    return i["score"]

def leaderboard(users):
    scores = [] # Compile the list of scores, like the list of users but each user has one score and multiple dictionaries
    for user in users:
        for score in user["scores"]:
            scores.append({"name": user["name"], "score": score})
    
    scores.sort(reverse=True, key=spec_sort)

    print("Leaderboard:") # Display leaderboard
    for i, score in enumerate(scores, start=1):
        if i <= 10:
            print(f"{i}. {score["name"]}: {score["score"]}")

#---------- END OF AVERY'S CODE (Leaderboard) ----------