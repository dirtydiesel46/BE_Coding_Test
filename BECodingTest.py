import re

def main():
    # Read the file "sampleInput.txt"
    with open("sampleInput.txt") as f:
        teams = f.read()
    f.close()

    # seperate matches from file into a list of matches per line
    matches = teams.split("\n")
    # create a dictionary containing teams
    teams = {}
    # loop through each match and add the teams to the dictionary with their points as per instruction ,
    # 3 for a win, 1 for a tie and 0 for a loss
    for match in matches:
        team1points = 0
        team2points = 0
        # split the match into two teams
        team1, team2 = match.split(",")
        # remove leading and trailing spaces from team names
        tempteam1name = team1.strip()
        tempteam2name = team2.strip()
        # split the team names into a list of words to find any team names containing spaces in between
        # e.g. FC Awesome
        tempt1name = tempteam1name.split(" ")
        tempt2name = tempteam2name.split(" ")
        # Check for the spaces, and then join the names back together
        # - else use the regex to extract the team name
        if len(tempt1name) > 2:
            tempt1name[0] = tempt1name[0] + " " + tempt1name[1]
        else:
            tempt1name[0] = "".join(re.split("[^a-zA-Z]*", team1))
        if len(tempt2name) > 2:
            tempt2name[0] = tempt2name[0] + " " + tempt2name[1]
        else:
            tempt2name[0] = "".join(re.split("[^a-zA-Z]*", team2))

        # Use regex to extract team scores
        team1score = "".join(re.split("[^0-9]*", team1))
        team2score = "".join(re.split("[^0-9]*", team2))
        # setup team names after concatenation of the strings or regex
        team1name = tempt1name[0]
        team2name = tempt2name[0]

        # rules to be followed for points, win == 3, tie == 1, loss == 0
        if team1score > team2score:
            print(team1name, "wins!")
            team1points += 3
        elif team1score < team2score:
            print(team2name, "wins!")
            team2points += 3
        else:
            print("It's a tie!")
            team1points += 1
            team2points += 1

        # add the points to the dictionary, check if team exists in dictionary first, if not add
        # - else , add points to team in dictionary
        if team1name not in teams:
            teams[team1name] = [team1name, team1points]
        else:
            teams[team1name][1] += team1points
        if team2name not in teams:
            teams[team2name] = [team2name, team2points]
        else:
            teams[team2name][1] += team2points

    # sort the dictionary by points, then write the teams line per line in order of points to the output.txt file
    sortedteams = sorted(teams.items(), key=lambda x: x[1][1], reverse=True)
    with open("output.txt", "w") as f:
        for team in sortedteams:
            team = team[0] + "".join(", ") + str(team[1][1]) + " pts"
            f.write(team)
            f.write("\n")
        f.close()

main()
