# teams compete in a round robin, where each team faces off against
# all other teams. Only two teams compete against each other at a time, and for team
# each competition, one team is designated the home team, the other is the away team

# In each competition there's always one winner and one loser
# no ties
# a team receives 3 points if it wins and 0 if it loses
# The competition array has elements in the form of [homeTeam, awayTeam]
# The results array contains info about the winner of each corresponding competition
# in the competitions array

# results[i] denotes the winner of competitions[i], where a 1 in the results means that the home team won and a 0
#  means that the away team won

# O(n) T n: num of competitions
# O(k) S

HOME_TEAM_WON = 1 # for better readability
def tournamentWinner(competitions, results):
    currentBestTeam = "" # to keep track of highest score so we don't need another loop for doing that
    scores = {currentBestTeam: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]

        homeTeam, awayTeam = competition # decomposition
        # figure out which team is homeTeam and which team is awayTeam
        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

        updateScores(winningTeam, 3, scores)
        if scores[currentBestTeam] < scores[winningTeam]:
            currentBestTeam = winningTeam

    return currentBestTeam


def updateScores(team, points, scores):
    if team not in scores:
        scores[team] = 0 # initialize the team that does not exist in the scores with 0 value
    scores[team] += points


# My Notes

# Decomposition in Python in the context of unpacking: This involves breaking down data structures like tuples, lists, or dictionaries into individual variables.