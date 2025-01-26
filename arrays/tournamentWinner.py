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

HOME_TEAM_WON = 1 # for better readability
def tournamentWinner(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition # decomposition

        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

        updateScores(winningTeam, 3, scores)

    return currentBestTeam


def updateScores():
    pass
