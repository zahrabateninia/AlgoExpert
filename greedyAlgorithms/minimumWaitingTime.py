# Prompt: you're given a non-empty array of positive ints representing the amounts of time
# that specific queries take to execute
# ONly one query can be executed at a time,m but the queries can be executed oin any order
# a query's waiting time: the amount of time that it must wait before its execution starts
# you can mutate the given array


# O(nLogn + n) = O(nLogn) T | O(1) S

def minimumWaitingTime(queries):
    queries.sort()
    totalWaitingTime = 0

    queriesNum = len(queries)
    for idx, duration in enumerate(queries):
        leftQueriesNum = queriesNum - (idx + 1)
        totalWaitingTime = duration * leftQueriesNum + totalWaitingTime
    
    return totalWaitingTime 

