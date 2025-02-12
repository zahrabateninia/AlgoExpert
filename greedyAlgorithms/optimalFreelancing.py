# Write a function that returns the max profit that can be obtained in a 7-day period
# Each job will take one full day to complete
# Only one job can be worked on at a time

# Sample input:
# jobs = {
#     {"deadline":1, "payment":1},
#     {"deadline":2, "payment":1},
#     {"deadline":2, "payment":2},
# } sample output: 3

# O(n Log(n)) T| O(1) S , n is num of jobs

def optimalFreelancing(jobs):
    LENGTH_OF_WEEK = 7
    profit = 0
    jobs.sort(key = lambda job: job["payment"], reverse=True) 

    # what days are still available -> True 
    timeline = [False] * LENGTH_OF_WEEK # an array of boolean 
    for job in jobs: # O(n) for loop
        # what is the latest possible time in the timeline that we can put it at
        # max time we consider
        maxTime = min(job["deadline"], LENGTH_OF_WEEK)
        for time in reversed(range(maxTime)): # it does not affect the time complexity 
            if timeline[time] == False:
                timeline[time] = True
                profit += jobs["payment"]
                break # continue the outer for loop
    return profit